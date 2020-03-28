#!/bin/bash

for mass in {200,250,300,350,400,450,500,600}
do
    echo $mass
    cat > crabconfigs/sigconfig/${mass}N.py <<EOF
from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'Wgamma949Signal17_${mass}_0p01%s'%"Jan16"
config.General.workArea = 'crab_jobs_signal%s'%"Jan16"
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.allowUndistributedCMSSW = True
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'config_genericMC.py'

config.JobType.sendExternalFolder = True
config.Data.inputDataset = '/MadGraphChargedResonance_WGToJJG_M${mass}_width0p01/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM'
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 5

config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = False
config.Data.outputDatasetTag = 'Wgamma949Signal17_${mass}_0p01%s'%"Jan16"
config.Site.storageSite = 'T3_US_Brown'
          
EOF
    crab submit crabconfigs/sigconfig/${mass}N.py 
done