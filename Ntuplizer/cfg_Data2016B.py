###### Process initialization ##########
import sys
import FWCore.ParameterSet.Config as cms

process = cms.Process("Ntuple")

process.load("Configuration.StandardSequences.MagneticField_cff")
process.load('Configuration.Geometry.GeometryRecoDB_cff')

process.TFileService = cms.Service("TFileService",
                                    fileName = cms.string('flatTuple.root')
                                   )

from VgammaTuplizer.Ntuplizer.ntuplizerOptions_data2016_cfi import config
#from VgammaTuplizer.Ntuplizer.ntuplizerOptions_generic_cfi import config

				   
####### Config parser ##########
import FWCore.ParameterSet.VarParsing as VarParsing

options = VarParsing.VarParsing ('analysis')
options.maxEvents = -1

#data file
#options.inputFiles = ('file://7AD20C58-263B-D646-9C54-105898A457F9.root')
                     
options.parseArguments()

process.options  = cms.untracked.PSet( 
                     wantSummary = cms.untracked.bool(True),
                     SkipEvent = cms.untracked.vstring('ProductNotFound'),
                     allowUnscheduled = cms.untracked.bool(True)
                     )

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(options.maxEvents) )

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(options.inputFiles),
#                            eventsToProcess = cms.untracked.VEventRange('282917:76757818-282917:76757820'),
#                            lumisToProcess = cms.untracked.VLuminosityBlockRange('282917:126'),
#                            skipEvents = cms.untracked.uint32(25385),
                            )                     


print " process source filenames %s" %(process.source) 
######## Sequence settings ##########

# https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookMiniAOD2015#ETmiss_filters
# For the RunIISpring15DR74 MC campaing, the process name in PAT.
# For Run2015B PromptReco Data, the process name is RECO.
# For Run2015B re-MiniAOD Data 17Jul2015, the process name is PAT.
hltFiltersProcessName = 'RECO'
if config["RUNONMC"] or config["JSONFILE"].find('reMiniAOD') != -1:
  hltFiltersProcessName = 'PAT'


# ####### Logger ##########
process.load("FWCore.MessageLogger.MessageLogger_cfi")

process.MessageLogger.cerr.threshold = 'INFO'
process.MessageLogger.categories.append('Ntuple')
process.MessageLogger.cerr.INFO = cms.untracked.PSet(
    limit = cms.untracked.int32(1)
)

process.MessageLogger.cerr.FwkReport.reportEvery = 500

####### Define conditions ##########
#process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
from Configuration.AlCa.GlobalTag import GlobalTag

GT = ''
if config["RUNONMC"]: GT = '102X_mcRun2_asymptotic_v8'
elif config["RUNONdata"]: GT = '102X_dataRun2_v13' ## change me for 2018D: 102X_dataRun2_Prompt_v16

print "*************************************** GLOBAL TAG *************************************************" 
print GT
print "****************************************************************************************************" 
process.GlobalTag = GlobalTag(process.GlobalTag, GT)

from RecoEgamma.EgammaTools.EgammaPostRecoTools import setupEgammaPostRecoSeq
setupEgammaPostRecoSeq(process,
                       runVID=True,
                       runEnergyCorrections=False, #no point in re-running them, they are already fine
                       era='2016-Legacy')  #era is new to select between 2016 / 2017,  it defaults to 2017

jetcorr_levels=[]
jetcorr_levels_groomed=[]
if config["RUNONMC"]:
  jetcorr_levels = cms.vstring(['L1FastJet', 'L2Relative', 'L3Absolute'])
  jetcorr_levels_groomed = cms.vstring(['L2Relative', 'L3Absolute']) # NO L1 corretion for groomed jets
else:
  jetcorr_levels = cms.vstring(['L1FastJet', 'L2Relative', 'L3Absolute', 'L2L3Residual'])
  jetcorr_levels_groomed = cms.vstring(['L2Relative', 'L3Absolute', 'L2L3Residual'])

   
######### read JSON file for data ##########					                                                             
if not(config["RUNONMC"]) and config["USEJSON"]:

  import FWCore.PythonUtilities.LumiList as LumiList
  import FWCore.ParameterSet.Types as CfgTypes
  process.source.lumisToProcess = CfgTypes.untracked(CfgTypes.VLuminosityBlockRange())
  myLumis = LumiList.LumiList(filename = config["JSONFILE"]).getCMSSWString().split(',')
  process.source.lumisToProcess.extend(myLumis) 

  if config["FILTEREVENTS"]:
  
   fname = ""
   if (options.inputFiles)[0].find("SingleMuon") != -1: fname = "RunLumiEventLists/SingleMuon_csc2015_Nov14.txt"
   elif (options.inputFiles)[0].find("SingleElectron") != -1: fname = "RunLumiEventLists/SingleElectron_csc2015_Nov14.txt"
   elif (options.inputFiles)[0].find("JetHT") != -1: fname = "RunLumiEventLists/JetHT_csc2015_Nov27.txt"
   else:
    print "** WARNING: EVENT LIST NOT FOUND! exiting... "
    sys.exit()
   
   print "** FILTERING EVENT LIST: %s" %fname 
   listEventsToSkip = []
   fileEventsToSkip = open(fname,"r")

   for line in fileEventsToSkip:
     cleanLine = line.rstrip()
     listEventsToSkip.append(cleanLine+"-"+cleanLine)

   rangeEventsToSkip = cms.untracked.VEventRange(listEventsToSkip)
   process.source.eventsToSkip = rangeEventsToSkip

####### Redo Jet clustering sequence ##########
betapar = cms.double(0.0)
fatjet_ptmin = 100.0

from RecoJets.Configuration.RecoPFJets_cff import *
from RecoJets.JetProducers.AnomalousCellParameters_cfi import *
from RecoJets.JetProducers.PFJetParameters_cfi import *

from PhysicsTools.PatAlgos.tools.helpers import *
pattask = getPatAlgosToolsTask(process)
                                                                                                          

if config["GETJECFROMDBFILE"]:
  process.load("CondCore.DBCommon.CondDBCommon_cfi")
  process.jec = cms.ESSource("PoolDBESSource",
            DBParameters = cms.PSet(
                messageLevel = cms.untracked.int32(5)
                ),
            timetype = cms.string('runnumber'),
            toGet = cms.VPSet(
            cms.PSet(
                 record = cms.string('JetCorrectionsRecord'),
                 tag    = cms.string('JetCorrectorParametersCollection_Summer15_50nsV5_MC_AK4PFchs'),
                 label  = cms.untracked.string('AK4PFchs')
                 ),
            cms.PSet(
                 record = cms.string('JetCorrectionsRecord'),
                 tag    = cms.string('JetCorrectorParametersCollection_Summer15_50nsV5_MC_AK8PFchs'),
                 label  = cms.untracked.string('AK8PFchs')
                 ),
            cms.PSet(
                 record = cms.string('JetCorrectionsRecord'),
                 tag    = cms.string('JetCorrectorParametersCollection_Summer15_50nsV5_MC_AK8PFPuppi'),
                 label  = cms.untracked.string('AK8PFPuppi')
                 ),
            ),
            connect = cms.string('sqlite:JEC/Summer15_50nsV5_MC.db')
            )
  if not config["RUNONMC"]:
    process.jec.toGet[0].tag =  cms.string('JetCorrectorParametersCollection_Summer15_50nsV5_DATA_AK4PFchs')
    process.jec.toGet[1].tag =  cms.string('JetCorrectorParametersCollection_Summer15_50nsV5_DATA_AK8PFchs')
    process.jec.toGet[2].tag =  cms.string('JetCorrectorParametersCollection_Summer15_50nsV5_DATA_AK8PFPuppi')
    process.jec.connect = cms.string('sqlite:JEC/Summer15_50nsV5_DATA.db')
  process.es_prefer_jec = cms.ESPrefer('PoolDBESSource','jec')



####### Add AK8 GenJets ##########
if config["ADDAK8GENJETS"]:

  from RecoJets.Configuration.RecoGenJets_cff import ak8GenJets
  addToProcessAndTask('ak8GenJets',
                      ak8GenJets.clone(src = 'packedGenParticles'),
                      process,pattask
                      )
  
  
  addToProcessAndTask('NjettinessGenAK8',
                      cms.EDProducer("NjettinessAdder",
                                     src=cms.InputTag("ak8GenJets"),
                                     Njets=cms.vuint32(1,2,3,4),          # compute 1-, 2-, 3-, 4- subjettiness
                                     # variables for measure definition : 
                                     measureDefinition = cms.uint32( 0 ), # CMS default is normalized measure
                                     beta = cms.double(1.0),              # CMS default is 1
                                     R0 = cms.double( 0.8 ),              # CMS default is jet cone size
                                     Rcutoff = cms.double( 999.0),       # not used by default
                                     # variables for axes definition :
                                       axesDefinition = cms.uint32( 6 ),    # CMS default is 1-pass KT axes
                                     nPass = cms.int32(999),             # not used by default
                                     akAxesR0 = cms.double(-999.0)        # not used by default
                                     ),
                      process,pattask
                      )
                      

  addToProcessAndTask('genParticlesForJets',
                      cms.EDProducer("InputGenJetsParticleSelector",
                                     src = cms.InputTag("packedGenParticles"),
                                     ignoreParticleIDs = cms.vuint32(1000022,
                                                                     1000012, 1000014, 1000016,
                                                                     2000012, 2000014, 2000016,
                                                                     1000039, 5100039,
                                                                     4000012, 4000014, 4000016,
                                                                     9900012, 9900014, 9900016,
                                                                     39),
                                     partonicFinalState = cms.bool(False),
                                     excludeResonances = cms.bool(False),
                                     excludeFromResonancePids = cms.vuint32(12, 13, 14, 16),
                                     tausAsJets = cms.bool(False)
                                     ),
                      process,pattask
                      )
           

  from RecoJets.JetProducers.SubJetParameters_cfi import SubJetParameters

  
  addToProcessAndTask('ak8GenJetsSoftDrop',
                      ak8GenJets.clone(SubJetParameters,
                                       useSoftDrop = cms.bool(True),
                                       R0 = cms.double(0.8),
                                       beta = betapar,
                                       writeCompound = cms.bool(True),
                                       jetCollInstanceName=cms.string("SubJets")
                                       ),
                      process,pattask
                      )
  

  
  
  addToProcessAndTask('ak8GenJetsSoftDropMass',
                      cms.EDProducer("RecoJetDeltaRValueMapProducer",
                                     src = cms.InputTag("ak8GenJets"),
                                     matched = cms.InputTag("ak8GenJetsSoftDrop"), 
                                     distMax = cms.double(0.8),
                                     value = cms.string('mass') 
                                     ),
                      process,pattask
                      )
  

  from VgammaTuplizer.Ntuplizer.redoPatJets_cff import patJetCorrFactorsAK8, patJetsAK8, selectedPatJetsAK8

  # Redo pat jets from gen AK8

  addToProcessAndTask('genJetsAK8',
                     patJetsAK8.clone( jetSource = 'ak8GenJets' ),
                     process,pattask)

  #process.genJetsAK8.userData.userFloats.src = [ cms.InputTag("ak8GenJetsPrunedMass"), cms.InputTag("ak8GenJetsSoftDropMass"), cms.InputTag("NjettinessGenAK8:tau1"), cms.InputTag("NjettinessGenAK8:tau2"), cms.InputTag("NjettinessGenAK8:tau3")]
  process.genJetsAK8.userData.userFloats.src = [ cms.InputTag("ak8GenJetsSoftDropMass"), cms.InputTag("NjettinessGenAK8:tau1"), cms.InputTag("NjettinessGenAK8:tau2"), cms.InputTag("NjettinessGenAK8:tau3")]
  process.genJetsAK8.addJetCorrFactors = cms.bool(False)
  process.genJetsAK8.jetCorrFactorsSource = cms.VInputTag( cms.InputTag("") )

  addToProcessAndTask('selectedGenJetsAK8',
                      selectedPatJetsAK8.clone( src = 'genJetsAK8', cut = cms.string('pt > 20') ),
                      process,pattask)

#### NEW NEW  JCH 3/24/20 ####
################# Update jets with b-tagging ######################
from PhysicsTools.PatAlgos.tools.jetTools import *

bTagDiscriminators=[  'pfBoostedDoubleSecondaryVertexAK8BJetTags',  'pfDeepDoubleBJetTags:probQ',  'pfDeepDoubleBJetTags:probH',  'pfDeepDoubleBvLJetTags:probQCD',  'pfDeepDoubleBvLJetTags:probHbb',  'pfDeepDoubleCvLJetTags:probQCD',  'pfDeepDoubleCvLJetTags:probHcc',  'pfDeepDoubleCvBJetTags:probHbb',  'pfDeepDoubleCvBJetTags:probHcc',  'pfMassIndependentDeepDoubleBvLJetTags:probQCD',  'pfMassIndependentDeepDoubleBvLJetTags:probHbb',  'pfMassIndependentDeepDoubleCvLJetTags:probQCD',  'pfMassIndependentDeepDoubleCvLJetTags:probHcc',  'pfMassIndependentDeepDoubleCvBJetTags:probHbb',  'pfMassIndependentDeepDoubleCvBJetTags:probHcc'  ]

from RecoBTag.MXNet.pfDeepBoostedJet_cff import pfDeepBoostedJetTags, pfMassDecorrelatedDeepBoostedJetTags, _pfDeepBoostedJetTagsAll

from RecoBTag.MXNet.Parameters.V02.pfDeepBoostedJetPreprocessParams_cfi import pfDeepBoostedJetPreprocessParams as pfDeepBoostedJetPreprocessParamsV02
from RecoBTag.MXNet.Parameters.V02.pfMassDecorrelatedDeepBoostedJetPreprocessParams_cfi import pfMassDecorrelatedDeepBoostedJetPreprocessParams as pfMassDecorrelatedDeepBoostedJetPreprocessParamsV02
pfDeepBoostedJetTags.preprocessParams = pfDeepBoostedJetPreprocessParamsV02
pfDeepBoostedJetTags.model_path = 'RecoBTag/Combined/data/DeepBoostedJet/V02/full/resnet-symbol.json'
pfDeepBoostedJetTags.param_path = 'RecoBTag/Combined/data/DeepBoostedJet/V02/full/resnet-0000.params'
pfMassDecorrelatedDeepBoostedJetTags.preprocessParams = pfMassDecorrelatedDeepBoostedJetPreprocessParamsV02
pfMassDecorrelatedDeepBoostedJetTags.model_path = 'RecoBTag/Combined/data/DeepBoostedJet/V02/decorrelated/resnet-symbol.json'
pfMassDecorrelatedDeepBoostedJetTags.param_path = 'RecoBTag/Combined/data/DeepBoostedJet/V02/decorrelated/resnet-0000.params'

process.slimmedJetsAK8Good = cms.EDFilter("PATJetSelector",
      src = cms.InputTag("slimmedJetsAK8"),
      cut = cms.string("pt>175 && isPFJet && abs(daughter(0).energy)!=exp(1000)"),
      #cut = cms.string("isPFJet && abs(daughter(0).energy)!=exp(1000)"),
)
fixedJets = cms.InputTag('slimmedJetsAK8Good')

if config["DODEEPAKX"]:
  print "deep akx activated"
  bTagDiscriminators=_pfDeepBoostedJetTagsAll + bTagDiscriminators

  #### something goes wrong with these taggers unless you do Kevin's trick:
  # https://github.com/TreeMaker/TreeMaker/blob/cee749aa26ae83dcd472ae2c5d282bd04fedda9c/TreeMaker/python/makeTreeFromMiniAOD_cff.py#L215-L218
print "calling updateJetCollection"
updateJetCollection(
    process,
    jetSource = fixedJets,
    pvSource = cms.InputTag('offlineSlimmedPrimaryVertices'),
    svSource = cms.InputTag('slimmedSecondaryVertices'),
    rParam = 0.8,
    jetCorrections = ('AK8PFPuppi', cms.vstring(['L2Relative', 'L3Absolute', 'L2L3Residual']), 'None'),
    btagDiscriminators = bTagDiscriminators,
    postfix = "VgRun2Tags"
   ) 

####### Adding HEEP id ##########

from PhysicsTools.SelectorUtils.tools.vid_id_tools import *

dataFormat=DataFormat.MiniAOD

####### Event filters ###########

##___________________________HCAL_Noise_Filter________________________________||
if config["DOHLTFILTERS"]:
 process.load('CommonTools.RecoAlgos.HBHENoiseFilterResultProducer_cfi')
 process.HBHENoiseFilterResultProducer.minZeros = cms.int32(99999)
 process.HBHENoiseFilterResultProducer.IgnoreTS4TS5ifJetInLowBVRegion=cms.bool(False) 
 ##___________________________BadChargedCandidate_Noise_Filter________________________________|| 
 process.load('Configuration.StandardSequences.Services_cff')
 process.load('RecoMET.METFilters.BadChargedCandidateFilter_cfi')
 # process.load('VgammaTuplizer.Ntuplizer.BadChargedCandidateFilter_cfi')
 process.BadChargedCandidateFilter.muons = cms.InputTag("slimmedMuons")
 process.BadChargedCandidateFilter.PFCandidates = cms.InputTag("packedPFCandidates")
 process.BadChargedCandidateFilter.debug = cms.bool(False)
 process.BadChargedCandidateSequence = cms.Sequence (process.BadChargedCandidateFilter)
 

####### Ntuplizer initialization ##########
jetsAK4 = "slimmedJets"
jetsAK8 = "slimmedJetsAK8" # should get overwritten below
# jetsAK8softdrop = "slimmedJetsAK8PFCHSSoftDropPacked" (if you want to add this subjet collection, changes need to be made in plugins/JetsNtuplizer.cc! Not needed to obtain subjets)
jetsAK8softdrop = ""
jetsAK8Puppi = ""  

METS = "slimmedMETs"
METS_EGclean = "slimmedMETsEGClean"
METS_MEGclean = "slimmedMETsMuEGClean"
METS_uncorr = "slimmedMETsUncorrected"

if config["DOMETRECLUSTERING"]: jetsAK4 = "selectedPatJets"
if config["USENOHF"]: METS = "slimmedMETsNoHF"  

##___________________ MET significance and covariance matrix ______________________##

if config["DOMETSVFIT"]:
  print "Using event pfMET covariance for SVfit"
  process.load("RecoMET.METProducers.METSignificance_cfi")
  process.load("RecoMET.METProducers.METSignificanceParams_cfi")
  pattask.add(process.METSignificance)

if config["DOMVAMET"]:
  from RecoMET.METPUSubtraction.jet_recorrections import recorrectJets
  recorrectJets(process, isData=True)
  
  from RecoMET.METPUSubtraction.MVAMETConfiguration_cff import runMVAMET
  runMVAMET( process, jetCollectionPF="patJetsReapplyJEC")
  process.MVAMET.srcLeptons  = cms.VInputTag("slimmedMuons", "slimmedElectrons", "slimmedTaus")
  process.MVAMET.requireOS = cms.bool(False)


TAUS = ""
BOOSTEDTAUS = ""
genAK8 = ""

if config["ADDAK8GENJETS"]:
  genAK8 = 'selectedGenJetsAK8'

if config["DOHBBTAGS"]:
  print "using updated PatJets"
  jetsAK8 = 'updatedPatJetsTransientCorrectedVgRun2Tags'
    

if config["DOTAUSBOOSTED"]:
#  TAUS = "slimmedTaus"
  TAUS = "NewTauIDsEmbedded"
  BOOSTEDTAUS = "slimmedTausBoosted"     
else:
#  TAUS = "slimmedTaus"
  TAUS = "NewTauIDsEmbedded"
  BOOSTEDTAUS = "slimmedTaus" 
  

######## JEC ########
jecLevelsAK8chs = []
jecLevelsAK8Groomedchs = []
jecLevelsAK4chs = []
jecLevelsAK4 = []
jecLevelsAK8Puppi = []
jecLevelsForMET = []

if config["BUNCHSPACING"] == 25 and config["RUNONMC"] :
   JECprefix = "Summer16_07Aug2017_V11"
   jecAK8chsUncFile = "JEC/%s_MC_Uncertainty_AK8PFPuppi.txt"%(JECprefix)
   #jecAK4chsUncFile = "JEC/%s_MC_Uncertainty_AK4PFchs.txt"%(JECprefix)
   jecAK4chsUncFile = "JEC/%s_MC_Uncertainty_AK4PFPuppi.txt"%(JECprefix)



elif config["BUNCHSPACING"] == 25 and not(config["RUNONMC"]):

   JEC_runDependent_suffix= "BCD"
  
   JECprefix = "Summer16_07Aug2017"+JEC_runDependent_suffix+"_V11"
   jecAK8chsUncFile = "JEC/%s_DATA_Uncertainty_AK8PFPuppi.txt"%(JECprefix)
   #jecAK4chsUncFile = "JEC/%s_DATA_Uncertainty_AK4PFchs.txt"%(JECprefix)
   jecAK4chsUncFile = "JEC/%s_DATA_Uncertainty_AK4PFPuppi.txt"%(JECprefix)
   print "jec JEC_runDependent_suffix %s ,  prefix %s " %(JEC_runDependent_suffix,JECprefix)

print "jec unc file for ak8 ", jecAK8chsUncFile
print "doing corrections to jets on th fly %s, to met on the fly %s" %(config["CORRJETSONTHEFLY"],config["CORRMETONTHEFLY"])
if config["CORRJETSONTHEFLY"]:
   if config["RUNONMC"]:
     jecLevelsAK8chs = [
     	 'JEC/%s_MC_L1FastJet_AK8PFPuppi.txt'%(JECprefix),
     	 'JEC/%s_MC_L2Relative_AK8PFPuppi.txt'%(JECprefix),
     	 'JEC/%s_MC_L3Absolute_AK8PFPuppi.txt'%(JECprefix)
       ]
     jecLevelsAK8Groomedchs = [
     	 'JEC/%s_MC_L2Relative_AK8PFPuppi.txt'%(JECprefix),
     	 'JEC/%s_MC_L3Absolute_AK8PFPuppi.txt'%(JECprefix)
       ]
     jecLevelsAK8Puppi = [
     	 'JEC/%s_MC_L2Relative_AK8PFPuppi.txt'%(JECprefix),
     	 'JEC/%s_MC_L3Absolute_AK8PFPuppi.txt'%(JECprefix)
       ]
     jecLevelsAK4chs = [
     	 #'JEC/%s_MC_L1FastJet_AK4PFPuppi.txt'%(JECprefix),
     	 'JEC/%s_MC_L2Relative_AK4PFPuppi.txt'%(JECprefix),
     	 'JEC/%s_MC_L3Absolute_AK4PFPuppi.txt'%(JECprefix)
       ]
   else:
     jecLevelsAK8chs = [
     	 'JEC/%s_DATA_L1FastJet_AK8PFPuppi.txt'%(JECprefix),
     	 'JEC/%s_DATA_L2Relative_AK8PFPuppi.txt'%(JECprefix),
     	 'JEC/%s_DATA_L3Absolute_AK8PFPuppi.txt'%(JECprefix),
         'JEC/%s_DATA_L2L3Residual_AK8PFPuppi.txt'%(JECprefix)
       ]
     jecLevelsAK8Groomedchs = [
     	 'JEC/%s_DATA_L2Relative_AK8PFPuppi.txt'%(JECprefix),
     	 'JEC/%s_DATA_L3Absolute_AK8PFPuppi.txt'%(JECprefix),
         'JEC/%s_DATA_L2L3Residual_AK8PFPuppi.txt'%(JECprefix)
       ]
     jecLevelsAK8Puppi = [
     	 'JEC/%s_DATA_L2Relative_AK8PFPuppi.txt'%(JECprefix),
     	 'JEC/%s_DATA_L3Absolute_AK8PFPuppi.txt'%(JECprefix),
         'JEC/%s_DATA_L2L3Residual_AK8PFPuppi.txt'%(JECprefix)
       ]
     jecLevelsAK4chs = [
     	 'JEC/%s_DATA_L1FastJet_AK4PFPuppi.txt'%(JECprefix),
     	 'JEC/%s_DATA_L2Relative_AK4PFPuppi.txt'%(JECprefix),
     	 'JEC/%s_DATA_L3Absolute_AK4PFPuppi.txt'%(JECprefix),
         'JEC/%s_DATA_L2L3Residual_AK4PFPuppi.txt'%(JECprefix)
       ]   
if config["CORRMETONTHEFLY"]:  
   if config["RUNONMC"]:
     jecLevelsForMET = [				       
     	 'JEC/%s_MC_L1FastJet_AK4PFchs.txt'%(JECprefix),
     	 'JEC/%s_MC_L2Relative_AK4PFchs.txt'%(JECprefix),
     	 'JEC/%s_MC_L3Absolute_AK4PFchs.txt'%(JECprefix)
       ]
   else:       					       
     jecLevelsForMET = [
     	 'JEC/%s_DATA_L1FastJet_AK4PFchs.txt'%(JECprefix),
     	 'JEC/%s_DATA_L2Relative_AK4PFchs.txt'%(JECprefix),
     	 'JEC/%s_DATA_L3Absolute_AK4PFchs.txt'%(JECprefix),
         'JEC/%s_DATA_L2L3Residual_AK4PFchs.txt'%(JECprefix)
       ]	
      			    
#Summer16_25nsV1b_DATA_PtResolution_AK8PFPuppi.txt
JERprefix = "Summer16_25nsV1b"
if config["RUNONMC"]:
  jerAK8chsFile_res = "JER/%s_MC_PtResolution_AK8PFchs.txt"%(JERprefix)
  jerAK4chsFile_res = "JER/%s_MC_PtResolution_AK4PFchs.txt"%(JERprefix)
  jerAK8PuppiFile_res = "JER/%s_MC_PtResolution_AK8PFPuppi.txt"%(JERprefix)
  jerAK4PuppiFile_res = "JER/%s_MC_PtResolution_AK4PFPuppi.txt"%(JERprefix)
  jerAK8chsFile_sf = "JER/%s_MC_SF_AK8PFchs.txt"%(JERprefix)
  jerAK4chsFile_sf = "JER/%s_MC_SF_AK4PFchs.txt"%(JERprefix)
  jerAK8PuppiFile_sf = "JER/%s_MC_SF_AK8PFPuppi.txt"%(JERprefix)
  jerAK4PuppiFile_sf = "JER/%s_MC_SF_AK4PFPuppi.txt"%(JERprefix)
else:
  jerAK8chsFile_res = "JER/%s_DATA_PtResolution_AK8PFchs.txt"%(JERprefix)
  jerAK4chsFile_res = "JER/%s_DATA_PtResolution_AK4PFchs.txt"%(JERprefix)
  jerAK8PuppiFile_res = "JER/%s_DATA_PtResolution_AK8PFPuppi.txt"%(JERprefix)
  jerAK4PuppiFile_res = "JER/%s_DATA_PtResolution_AK4PFPuppi.txt"%(JERprefix)
  jerAK8chsFile_sf = "JER/%s_DATA_SF_AK8PFchs.txt"%(JERprefix)
  jerAK4chsFile_sf = "JER/%s_DATA_SF_AK4PFchs.txt"%(JERprefix)
  jerAK8PuppiFile_sf = "JER/%s_DATA_SF_AK8PFPuppi.txt"%(JERprefix)
  jerAK4PuppiFile_sf = "JER/%s_DATA_SF_AK4PFPuppi.txt"%(JERprefix)

print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
print "Fatjet Collection: ", jetsAK8
print "PuppiJet Collection: ", jetsAK8Puppi
print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
                                                                                           
################## Ntuplizer ###################
process.ntuplizer = cms.EDAnalyzer("Ntuplizer",
    runOnMC	      = cms.bool(config["RUNONMC"]),
    doGenParticles    = cms.bool(config["DOGENPARTICLES"]),
    doGenJets	      = cms.bool(config["DOGENJETS"]),
    doGenEvent	      = cms.bool(config["DOGENEVENT"]),
    doPileUp	      = cms.bool(config["DOPILEUP"]),
    doElectrons       = cms.bool(config["DOELECTRONS"]),
    doPhotons         = cms.bool(config["DOPHOTONS"]),
    doMuons	      = cms.bool(config["DOMUONS"]),
    doTaus	      = cms.bool(config["DOTAUS"]),
    doAK8Jets	      = cms.bool(config["DOAK8JETS"]),
    doAK4Jets	      = cms.bool(config["DOAK4JETS"]),
    doVertices	      = cms.bool(config["DOVERTICES"]),
    doTriggerDecisions= cms.bool(config["DOTRIGGERDECISIONS"]),
    doTriggerObjects  = cms.bool(config["DOTRIGGEROBJECTS"]),
    doHltFilters      = cms.bool(config["DOHLTFILTERS"]),
    doMissingEt       = cms.bool(config["DOMISSINGET"]),
    #doHbbTagOLD	      = cms.bool(config["DOHBBTAGOLD"]),
    doHbbTags	      = cms.bool(config["DOHBBTAGS"]),
    doDeepAKX	      = cms.bool(config["DODEEPAKX"]),
    #doPrunedSubjets   = cms.bool(config["DOAK8PRUNEDRECLUSTERING"]),
    #doTrimming        = cms.bool(config["DOAK10TRIMMEDRECLUSTERING"]),
    #doPuppi           = cms.bool(config["DOAK8PUPPI"]),#NOT IS USE ANYMORE
    doBoostedTaus     = cms.bool(config["DOTAUSBOOSTED"]),
    doMETSVFIT        = cms.bool(config["DOMETSVFIT"]),
    doMVAMET          = cms.bool(config["DOMVAMET"]),
    doMultipleTauMVAversions = cms.bool(config["DOMULTIPLETAUMVAVERSIONS"]),
    vertices = cms.InputTag("offlineSlimmedPrimaryVertices"),
    muons = cms.InputTag("slimmedMuons"),
    photons = cms.InputTag("slimmedPhotons"),
    phoIdVerbose = cms.bool(False),
    electrons = cms.InputTag("slimmedElectrons"),
    ebRecHits = cms.InputTag("reducedEgamma","reducedEBRecHits"),

    dupCluster          = cms.InputTag("particleFlowEGammaGSFixed:dupECALClusters"),
    hitsNotReplaced     = cms.InputTag("ecalMultiAndGSGlobalRecHitEB:hitsNotReplaced"),
    taus = cms.InputTag(TAUS),
    tausBoostedTau = cms.InputTag(BOOSTEDTAUS),
    jets = cms.InputTag(jetsAK4),
    fatjets = cms.InputTag(jetsAK8),
    softdropjets = cms.InputTag(jetsAK8softdrop),
    puppijets = cms.InputTag(jetsAK8Puppi),
    genJets = cms.InputTag("slimmedGenJets"),
    genJetsAK8 = cms.InputTag(genAK8),
    subjetflavour = cms.InputTag("AK8byValAlgo"),
    mets = cms.InputTag(METS),
    mets_EGclean = cms.InputTag(METS_EGclean),
    mets_MEGclean = cms.InputTag(METS_MEGclean),
    mets_uncorr = cms.InputTag(METS_uncorr),
    mets_puppi = cms.InputTag("slimmedMETsPuppi"),
    mets_mva = cms.InputTag("MVAMET","MVAMET"),
    corrMetPx = cms.string("+0.1166 + 0.0200*Nvtx"),
    corrMetPy = cms.string("+0.2764 - 0.1280*Nvtx"),
    jecAK4forMetCorr = cms.vstring( jecLevelsForMET ),
    jetsForMetCorr = cms.InputTag(jetsAK4),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    genparticles = cms.InputTag("prunedGenParticles"),
    PUInfo = cms.InputTag("slimmedAddPileupInfo"),
    genEventInfo = cms.InputTag("generator"),
    externallheProducer = cms.InputTag("externalLHEProducer"),
    HLT = cms.InputTag("TriggerResults","","HLT"),
    triggerobjects = cms.InputTag("slimmedPatTrigger"),
    triggerprescales = cms.InputTag("patTrigger"),
    noiseFilter = cms.InputTag('TriggerResults','', hltFiltersProcessName),
    jecAK8chsPayloadNames = cms.vstring( jecLevelsAK8chs ),
    jecAK8chsUnc = cms.string( jecAK8chsUncFile ),
    #jecAK8GroomedchsPayloadNames = cms.vstring( jecLevelsAK8Groomedchs ),
    jecAK8GroomedchsPayloadNames = cms.vstring( jecLevelsAK8Groomedchs ),
    jecAK8PuppiPayloadNames = cms.vstring( jecLevelsAK8Puppi ),
    jecAK4chsPayloadNames = cms.vstring( jecLevelsAK4chs ),
    jecAK4chsUnc = cms.string( jecAK4chsUncFile ),
    jecpath = cms.string(''),
    jerAK8chs_res_PayloadNames = cms.string( jerAK8chsFile_res ),
    jerAK4chs_res_PayloadNames = cms.string( jerAK4chsFile_res ),
    jerAK8Puppi_res_PayloadNames = cms.string(  jerAK8PuppiFile_res ),
    jerAK4Puppi_res_PayloadNames = cms.string(  jerAK4PuppiFile_res ),
    jerAK8chs_sf_PayloadNames = cms.string( jerAK8chsFile_sf ),
    jerAK4chs_sf_PayloadNames = cms.string( jerAK4chsFile_sf ),
    jerAK8Puppi_sf_PayloadNames = cms.string(  jerAK8PuppiFile_sf ),
    jerAK4Puppi_sf_PayloadNames = cms.string(  jerAK4PuppiFile_sf ),

    
    ## Noise Filters ###################################
    # defined here: https://github.com/cms-sw/cmssw/blob/CMSSW_7_4_X/PhysicsTools/PatAlgos/python/slimming/metFilterPaths_cff.py
    noiseFilterSelection_HBHENoiseFilter = cms.string('Flag_HBHENoiseFilter'),
    #noiseFilterSelection_HBHENoiseFilterLoose = cms.InputTag("HBHENoiseFilterResultProducer", "HBHENoiseFilterResultRun2Loose"),
    #noiseFilterSelection_HBHENoiseFilterTight = cms.InputTag("HBHENoiseFilterResultProducer", "HBHENoiseFilterResultRun2Tight"),
    noiseFilterSelection_HBHENoiseIsoFilter = cms.InputTag("HBHENoiseFilterResultProducer", "HBHEIsoNoiseFilterResult"),    
    noiseFilterSelection_CSCTightHaloFilter = cms.string('Flag_CSCTightHaloFilter'),
    #noiseFilterSelection_CSCTightHalo2015Filter = cms.string('Flag_CSCTightHalo2015Filter'),
    #noiseFilterSelection_hcalLaserEventFilter = cms.string('Flag_hcalLaserEventFilter'),
    noiseFilterSelection_EcalDeadCellTriggerPrimitiveFilter = cms.string('Flag_EcalDeadCellTriggerPrimitiveFilter'),
    noiseFilterSelection_goodVertices = cms.string('Flag_goodVertices'),
    #noiseFilterSelection_trackingFailureFilter = cms.string('Flag_trackingFailureFilter'),
    noiseFilterSelection_eeBadScFilter = cms.string('Flag_eeBadScFilter'),
    #noiseFilterSelection_ecalLaserCorrFilter = cms.string('Flag_ecalLaserCorrFilter'),
    #noiseFilterSelection_trkPOGFilters = cms.string('Flag_trkPOGFilters'),
    #
    ##New for ICHEP 2016
    #noiseFilterSelection_CSCTightHaloTrkMuUnvetoFilter = cms.string('Flag_CSCTightHaloTrkMuUnvetoFilter'),
    #noiseFilterSelection_globalTightHalo2016Filter = cms.string('Flag_globalTightHalo2016Filter'),
    noiseFilterSelection_globalSuperTightHalo2016Filter = cms.string('Flag_globalSuperTightHalo2016Filter'),
    #noiseFilterSelection_HcalStripHaloFilter = cms.string('Flag_HcalStripHaloFilter'),
    #noiseFilterSelection_chargedHadronTrackResolutionFilter = cms.string('Flag_chargedHadronTrackResolutionFilter'),
    #noiseFilterSelection_muonBadTrackFilter = cms.string('Flag_muonBadTrackFilter'),
    #
    ##New for Moriond
    #noiseFilterSelection_badMuonsFilter = cms.string('Flag_badMuons'),
    #noiseFilterSelection_duplicateMuonsFilter = cms.string('Flag_duplicateMuons'),
    #noiseFilterSelection_nobadMuonsFilter = cms.string('Flag_nobadMuons'),

    ## and the sub-filters
    #noiseFilterSelection_trkPOG_manystripclus53X = cms.string('Flag_trkPOG_manystripclus53X'),
    #noiseFilterSelection_trkPOG_toomanystripclus53X = cms.string('Flag_trkPOG_toomanystripclus53X'),
    #noiseFilterSelection_trkPOG_logErrorTooManyClusters = cms.string('Flag_trkPOG_logErrorTooManyClusters'),
    # summary
    noiseFilterSelection_metFilters = cms.string('Flag_METFilters'),

    packedpfcandidates = cms.InputTag('packedPFCandidates')
)


####### Final path ##########
process.p = cms.Path()
process.p += process.egammaPostRecoSeq
process.p += process.slimmedJetsAK8Good
if config["DOHLTFILTERS"]:
 process.p += process.HBHENoiseFilterResultProducer
 process.p += process.BadChargedCandidateSequence

#process.p += process.egmPhotonIDSequence
# For new MVA ID END!

process.p += process.ntuplizer
process.p.associate(pattask)

print pattask
print process
print process.p
