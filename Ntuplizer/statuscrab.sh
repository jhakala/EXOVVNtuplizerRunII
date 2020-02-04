#!/bin/bash

for mass in {200,250,300,350,400,450,500,600}
do
    crab status -d /afs/cern.ch/work/x/xuyan/work5/PROD17/CMSSW_9_4_9/src/VgammaTuplizer/Ntuplizer/crab_jobs_signalJan16/crab_Wgamma949Signal17_${mass}_0p01Jan16
done

#narriw 300 1800 invalid
#wide 400 3000
