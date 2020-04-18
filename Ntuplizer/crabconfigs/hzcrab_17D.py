from CRABClient.UserUtilities import config, getUsernameFromCRIC
config = config()

config.General.requestName = 'HZgamma94XSinglePhoton_%s_2017D'%"Apr8"
config.General.workArea = 'crab_jobs_2017D_photon%s'%"Apr8"
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.allowUndistributedCMSSW = True
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'cfg_Data2017DE.py'
config.JobType.inputFiles=[
        'JSON/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSONv1.txt'
]
config.JobType.sendExternalFolder = True
config.Data.inputDataset = '/SinglePhoton/Run2017D-31Mar2018-v1/MINIAOD'
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 3
config.Data.lumiMask='JSON/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSONv1.txt'
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromCRIC())
config.Data.publication = False
config.Data.outputDatasetTag = 'HZgamma94XSinglePhoton_%s_2017D'%"Apr8"
config.Site.storageSite = 'T3_US_Brown'
