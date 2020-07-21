from CRABClient.UserUtilities import config, getUsernameFromCRIC
config = config()

config.General.requestName = 'HZgamma102XSinglePhoton_%s_2016D'%"Jul9"
config.General.workArea = 'crab_jobs_2016D_photon%s'%"Jul9"
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.allowUndistributedCMSSW = True
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'cfg_Data2016D.py'
config.JobType.inputFiles=[
        'JSON/Cert_271036-284044_13TeV_ReReco_07Aug2017_Collisions16_JSON.txt'
]
config.JobType.sendExternalFolder = True
config.Data.inputDataset = '/SinglePhoton/Run2016D-17Jul2018-v1/MINIAOD'
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 2
config.Data.lumiMask='JSON/Cert_271036-284044_13TeV_ReReco_07Aug2017_Collisions16_JSON.txt'
config.Data.outLFNDirBase = '/store/group/lpcboostres/' 
config.Data.publication = False
config.Data.outputDatasetTag = 'HZgamma102XSinglePhoton_%s_2016D'%"Jul9"
config.Site.storageSite = 'T3_US_FNALLPC'
