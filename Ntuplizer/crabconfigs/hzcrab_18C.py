from CRABClient.UserUtilities import config, getUsernameFromCRIC
config = config()

config.General.requestName = 'HZgamma102XEGamma_%s_2018C'%"June8"
config.General.workArea = 'crab_jobs_2018C_photon%s'%"June8"
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.allowUndistributedCMSSW = True
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'cfg_Data2018C.py'
config.JobType.inputFiles=[
        'JSON/Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON.txt'
]
config.JobType.sendExternalFolder = True
config.Data.inputDataset = '/EGamma/Run2018C-17Sep2018-v1/MINIAOD'
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 2
config.Data.lumiMask='JSON/Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON.txt'
config.Data.outLFNDirBase = '/store/group/lpcboostres/' 
config.Data.publication = False
config.Data.outputDatasetTag = 'HZgamma102XEGamma_%s_2018C'%"June8"
config.Site.storageSite = 'T3_US_FNALLPC'
