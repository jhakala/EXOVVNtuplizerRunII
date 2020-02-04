#!/bin/bash
for mass in {200,250,300,350,400,450,500,600,700,800,900,1000,1200,1400,1600,1800,2000,2200,2400,2600,2800,3000,3500}
do
    crab resubmit -d /afs/cern.ch/work/x/xuyan/work5/PROD17/CMSSW_9_4_9/src/VgammaTuplizer/Ntuplizer/crab_jobs_signalJan16/crab_Wgamma949Signal17_${mass}_0p01Jan16
done
