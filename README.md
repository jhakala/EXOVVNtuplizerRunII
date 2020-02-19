# EXO VGammaNtuplizerRunII

Ntuplizer for searches for heavy resonances decaying to boson + photon

## installation instructions

Setting up CMSSW (2017):

```
cmsrel CMSSW_9_4_13
cd CMSSW_9_4_13/src
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
git checkout -b "your new branch name" 949Wgam/94X_ntuplizer
cd $CMSSW_BASE/src
scram b -j 16
3. push code: use ssh, follow instructions on google
git push "remote name" "remote branch name"
```

PS: To clone code directly: git clone -b 949Wgam_prod17 https://github.com/xuliyan/VgammaTuplizer.git

### EGamma ID would be accessed via userfloat, all valuemap methods are deprecated
(https://twiki.cern.ch/twiki/bin/view/CMS/EgammaMiniAODV2)
```
cd $CMSSW_BASE/src
git cms-merge-topic cms-egamma:EgammaPostRecoTools #just adds in an extra file to have a setup function to make things easier
scram b -j 8
```


### running for data and MC

```
cmsRun config_generic<Era>.py 

```
