# EXO VGammaNtuplizerRunII

Ntuplizer for searches for heavy resonances decaying to boson + photon

## installation instructions

Setting up CMSSW (for september reprocessing):

```
cmsrel CMSSW_9_4_9
cd CMSSW_9_4_9/src
cmsenv
git cms-init
```

### getting the ntuplizer codes
```
1. Fork the repo to your area

2. 
cd $CMSSW_BASE/src
git clone https://github.com/"your github user name"/VgammaTuplizer.git
cd VgammaTuplizer
git remote add 94XWgam https://github.com/"your github user name"/VgammaTuplizer
git fetch 94XWgam
git checkout -b "your new branch name" 94XWgam/94X_ntuplizer
cd $CMSSW_BASE/src
scram b -j 16
3. push code: use ssh, follow instructions on google
git push "remote name" "remote branch name"
```

PS: To clone code directly: git clone -b 94XWgam_dev https://github.com/xuliyan/VgammaTuplizer.git

### update Egamma MVAID. HEEP are included by default in 94X
(https://twiki.cern.ch/twiki/bin/view/CMS/MultivariatePhotonIdentificationRun2#MVA_Recipe_for_regular_users_for) and
(https://twiki.cern.ch/twiki/bin/view/CMS/EgammaPostRecoRecipes#2016_2017_Data_MC)
```
cd $CMSSW_BASE/src
git cms-merge-topic cms-egamma:EgammaID_949
cd $CMSSW_BASE/src
scram b -j 8
```


### running for data and MC
Just set the proper flag in python/ntuplizerOptions_generic_cfi.py

```
cmsRun config_generic.py 

```


to recluster jets and MET, or to add the Higgs-tagger the following flags can be changed:
```
config["DOAK8RECLUSTERING"] = False
config["DOHBBTAG"] = False
config["DOAK8PRUNEDRECLUSTERING"] = False
config["DOMETRECLUSTERING"] = False
```
If you want to use Higgs tagger the first two flags must all be set to True.

### Batch submission

#### Config file creation

Config file creation can be done via the [createConfig.py](Ntuplizer/tools/createConfig.py) script. It requires a text file with a list of input data sets, see e.g. [samples/QCD_HT_RunIISpring15MiniAODv2.txt](Ntuplizer/samples/QCD_HT_RunIISpring15MiniAODv2.txt). To run:
```
python tools/createConfig.py samples/QCD_HT_RunIISpring15MiniAODv2.txt
```
When running over *data*, this requires the ```-d``` flag. The script will automatically determine if the data sets are available on the T3 storage element. Also, ```--help``` will provide more information (e.g. allows changing the default number of jobs per event). If you run the script from a different directory, you need to provide the location of the [template file](Ntuplizer/submitJobsOnT3batch.cfg).

#### Job submission

Submit your jobs using the [submitJobsOnT3batch.py](Ntuplizer/submitJobsOnT3batch.py) script with the generated config files like this:
```
python submitJobsOnT3batch.py -C myconfig.cfg
```
Once the jobs are done, they can be checked for completeness like this:
```
python submitJobsOnT3batch.py -C myconfig.cfg --check
```
Resubmit jobs like this:
```
python submitJobsOnT3batch.py -C myconfig.cfg --resubmit 1,4,7
```
And eventually copied to the SE (path given in the config file):
```
python submitJobsOnT3batch.py -C myconfig.cfg --copy
```

Finally, note that, when you run on crab, you have to enable 
```
config.JobType.sendExternalFolder = True
```
as described at https://twiki.cern.ch/twiki/bin/viewauth/CMS/MultivariateElectronIdentificationRun2#Recipes_and_implementation
