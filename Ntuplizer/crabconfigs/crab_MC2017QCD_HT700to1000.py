from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'Wgamma949_QCD_HT700to1000_%s'%"Aug02"
config.General.workArea = 'crab_jobs_WgammaMC_2017_%s'%"Aug02"
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'config_generic.py'

config.JobType.sendExternalFolder = True
config.Data.inputDataset = '/QCD_HT700to1000_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM'
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 30

config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = False
config.Data.outputDatasetTag = 'Wgamma949_QCD_HT700to1000_%s'%"Aug02"
config.Site.storageSite = 'T3_US_Brown'
