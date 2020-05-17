from CRABClient.UserUtilities import config, getUsernameFromCRIC
config = config()

config.General.requestName = 'HZgamma94XEGamma_%s_2018B'%"May17"
config.General.workArea = 'crab_jobs_2018B_photon%s'%"May17"
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.allowUndistributedCMSSW = True
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'cfg_Data2018B.py'
config.JobType.inputFiles=[
        'JSON/Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON.txt'
]
config.JobType.sendExternalFolder = True
config.Data.inputDataset = '/EGamma/Run2018B-17Sep2018-v1/MINIAOD'
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 2
config.Data.lumiMask='JSON/Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON.txt'
config.Data.outLFNDirBase = '/store/group/lpcboostres/' 
config.Data.publication = False
config.Data.outputDatasetTag = 'HZgamma94XEGamma_%s_2017B'%"May17"
config.Site.storageSite = 'T3_US_FNALLPC'
