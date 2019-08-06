from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'Wgamma949Signal4000_%s'%"Aug02"
config.General.workArea = 'crab_jobs_signal%s'%"Aug02"
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'config_generic.py'

config.JobType.sendExternalFolder = True
config.Data.inputDataset = '/PythiaChargedResonance_WGToJJG_M4000_width5/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM'
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1

config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = False
config.Data.outputDatasetTag = 'Wgamma949Signal4000_%s'%"Aug02"
config.Site.storageSite = 'T3_US_Brown'
