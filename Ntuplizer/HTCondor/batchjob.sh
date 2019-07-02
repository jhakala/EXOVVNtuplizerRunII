source /cvmfs/cms.cern.ch/cmsset_default.sh
export SCRAM_ARCH=slc6_amd64_gcc630
cd /afs/cern.ch/work/x/xuyan/work5/DEV/CMSSW_9_4_9/src/VgammaTuplizer/Ntuplizer
eval `scram runtime -sh`
cmsRun config_generic.py
