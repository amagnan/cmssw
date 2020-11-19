#!/usr/bin/env python

#Front of HGCAL
#for run in `seq 0 9`; do python submitProdStep.py -r $run -n 100 -s 12345$run -d CloseByPhotons -w 23293.0_CloseByParticleGun+2026D49+CloseByParticle_Photon_ERZRanges_GenSimHLBeamSpot+DigiTrigger+RecoGlobal+HARVESTGlobal/ -o ProdTicl -e /store/user/amagnan/HGCAL/TiCL ; done
#for run in `seq 0 9`; do python submitProdStep.py -r $run -n 100 -s 12345$run -d CloseByPhotonsWithPU -w 23493.0_CloseByParticleGun+2026D49PU+CloseByParticle_Photon_ERZRanges_GenSimHLBeamSpot+DigiTriggerPU+RecoGlobalPU+HARVESTGlobalPU/ --skip-step1 --config2=step2_DIGI_L1TrackTrigger_L1_DIGI2RAW_HLT_PU.py --config3=step3_RAW2DIGI_L1Reco_RECO_RECOSIM_PAT_VALIDATION_DQM_PU.py -o ProdTicl -E /store/user/amagnan/HGCAL/TiCL/CloseByPhotons -e /store/user/amagnan/HGCAL/TiCL ; done
#from Vtx
#for run in `seq 0 9`; do python submitProdStep.py -r $run -n 100 -s 12346$run -d CloseByPhotonsFromVtx -w 23293.0_CloseByParticleGun+2026D49+CloseByParticle_Photon_ERZRanges_GenSimHLBeamSpot+DigiTrigger+RecoGlobal+HARVESTGlobal/ --config1=CloseByParticle_Photon_ERZRanges_from0_cfi_GEN_SIM.py -o ProdTicl -e /store/user/amagnan/HGCAL/TiCL ; done
#for run in `seq 0 9`; do python submitProdStep.py -r $run -n 100 -s 12346$run -d CloseByPhotonsFromVtxWithPU -w 23493.0_CloseByParticleGun+2026D49PU+CloseByParticle_Photon_ERZRanges_GenSimHLBeamSpot+DigiTriggerPU+RecoGlobalPU+HARVESTGlobalPU/ --skip-step1 --config2=step2_DIGI_L1TrackTrigger_L1_DIGI2RAW_HLT_PU.py --config3=step3_RAW2DIGI_L1Reco_RECO_RECOSIM_PAT_VALIDATION_DQM_PU.py -o ProdTicl -E /store/user/amagnan/HGCAL/TiCL/CloseByPhotonsFromVtx -e /store/user/amagnan/HGCAL/TiCL ; done

#Front of HGCAL - fixed pT/eta
#for run in `seq 0 9`; do python submitProdStep.py -r $run -n 100 -s 12345$run -d CloseByPhotons -w 23293.0_CloseByParticleGun+2026D49+CloseByParticle_Photon_ERZRanges_GenSimHLBeamSpot+DigiTrigger+RecoGlobal+HARVESTGlobal/ --config3=../step3_EMiterOnly_noPU.py -o ProdTiclEM -e /store/user/amagnan/HGCAL/TiCL/EMonly --minpT=4.95 --maxpT=5.05 --minEta=1.69 --maxEta=1.71 --minz=320 --PtEta=pt5_eta17; done
#for run in `seq 0 9`; do python submitProdStep.py -r $run -n 100 -s 12345$run -d CloseByPhotonsWithPU -w 23493.0_CloseByParticleGun+2026D49PU+CloseByParticle_Photon_ERZRanges_GenSimHLBeamSpot+DigiTriggerPU+RecoGlobalPU+HARVESTGlobalPU/ --skip-step1 --config2=step2_DIGI_L1TrackTrigger_L1_DIGI2RAW_HLT_PU.py --config3=../step3_EMiterOnly_PU.py  -o ProdTiclEM -E /store/user/amagnan/HGCAL/TiCL/EMonly/CloseByPhotons -e /store/user/amagnan/HGCAL/TiCL/EMonly  --PtEta=pt5_eta17 ; done
#for run in `seq 0 9`; do python submitProdStep.py -r $run -n 100 -s 12346$run -d CloseByPhotonsFromVtx -w 23293.0_CloseByParticleGun+2026D49+CloseByParticle_Photon_ERZRanges_GenSimHLBeamSpot+DigiTrigger+RecoGlobal+HARVESTGlobal/ --config3=../step3_EMiterOnly_noPU.py -o ProdTiclEM -e /store/user/amagnan/HGCAL/TiCL/EMonly --minpT=4.95 --maxpT=5.05 --minEta=1.69 --maxEta=1.71 --minz=0 --PtEta=pt5_eta17; done

#for eta in 17 19 21 23 25 27; do for pT in 3 5 10 15 20 30 40 50 75 100 150 200; do for run in `seq 0 9`; do python submitProdStep.py -r $run -n 100 -s ${pT}${eta}${run} -d CloseByPhotons -w 23293.0_CloseByParticleGun+2026D49+CloseByParticle_Photon_ERZRanges_GenSimHLBeamSpot+DigiTrigger+RecoGlobal+HARVESTGlobal/ --config3=../step3_EMiterOnly_noPU.py -o ProdTiclEMNew -e /store/user/amagnan/HGCAL/TiCL/EMonlyNew --pT=${pT} --Eta=${eta} --minz=320 --PtEta=pt${pT}_eta${eta} -R 0;  done; done; done

#step TiCL only
#for eta in 17; do for pT in 3 5 10; do for run in `seq 0 9`; do python submitProdStep.py -r $run -n 100 -s ${pT}${eta}${run} -d CloseByPhotons  --skip-step1  --skip-step2  --skip-step3 --configTicl=step3ticl_noPU.py  -o ProdTiclEMNew -e /store/user/amagnan/HGCAL/TiCL/EMonlyNew -E /store/user/amagnan/HGCAL/TiCL/EMonlyNew/CloseByPhotons --pT=${pT} --Eta=${eta} --minz=320 --PtEta=pt${pT}_eta${eta} -R 0;  done; done; done

import subprocess
import os,sys
import optparse
import commands
import math
import random

usage = 'usage: %prog [options]'
parser = optparse.OptionParser(usage)
parser.add_option('-r', '--run'         ,    dest='run'                , help='stat run'                     , default=-1 ,      type=int)
parser.add_option('-R', '--firstRun'    ,    dest='firstRun'           , help='first run for grid proxy'     , default=1  ,      type=int)
parser.add_option('-n', '--nevts'       ,    dest='nevts'              , help='number of events to generate' , default=100,      type=int)
parser.add_option('-s', '--randomSeed'  ,    dest='randomSeed'         , help='random seed for generator process' , default=123456,    type=int)
parser.add_option('-d', '--datatype'    ,    dest='datatype'           , help='data type or particle to shoot', default='CloseByPhotons')
parser.add_option('-w', '--workflow'    ,    dest='workflow'           , help='Directory of workflow from runTheMatrix', default='23293.0_CloseByParticleGun+2026D49+CloseByParticle_Photon_ERZRanges_GenSimHLBeamSpot+DigiTrigger+RecoGlobal+HARVESTGlobal')
parser.add_option('--config1'      ,  dest='config1'           , help='Step1 config file to run', default='CloseByParticle_Photon_ERZRanges_cfi_GEN_SIM.py')
parser.add_option('--config2'      ,  dest='config2'           , help='Step2 config file to run', default='step2_DIGI_L1TrackTrigger_L1_DIGI2RAW_HLT.py')
parser.add_option('--config3'      ,  dest='config3'           , help='Step3 config file to run', default='step3_RAW2DIGI_L1Reco_RECO_RECOSIM_PAT_VALIDATION_DQM.py')
parser.add_option('--configTicl'      ,  dest='configTicl'           , help='Step3 config file to rerun just TICL', default='step3ticl_noPU.py')
parser.add_option('-o', '--out'         ,    dest='out'                , help='output directory'             , default=os.getcwd() )
parser.add_option('-e', '--eosout'         ,    dest='eosout'                , help='eos path to save root file to EOS',         default='')
parser.add_option('-E', '--eosin'         ,    dest='eosin'                , help='eos path to read input root file from EOS',         default='')
parser.add_option('-S', '--no-submit'   ,    action="store_true",  dest='nosubmit'           , help='Do not submit batch job.')
parser.add_option('--skip-step1'   ,    action="store_true",  dest='skipStep1'           , help='Skip first step: copy step1 file from eos.')
parser.add_option('--skip-step2'   ,    action="store_true",  dest='skipStep2'           , help='Skip second step: copy step2 file from eos.')
parser.add_option('--skip-step3'   ,    action="store_true",  dest='skipStep3'           , help='Skip third step: copy step3 file from eos and rerun TICL.')

parser.add_option('--pT'  ,    dest='pT'         , help='pT for generator process' , default=5,    type=float)
parser.add_option('--minpT'  ,    dest='minpT'         , help='Minimum pT for generator process' , default=4.95,    type=float)
parser.add_option('--maxpT'  ,    dest='maxpT'         , help='Maximum pT for generator process' , default=5.05,    type=float)
parser.add_option('--Eta'  ,    dest='Eta'         , help='Eta*10 for generator process' , default=17,    type=float)
parser.add_option('--minEta'  ,    dest='minEta'         , help='Minimum Eta for generator process' , default=1.69,    type=float)
parser.add_option('--maxEta'  ,    dest='maxEta'         , help='Maximum Eta for generator process' , default=1.71,    type=float)
parser.add_option('--minz'  ,    dest='minz'         , help='Minimum z for generator process' , default=320,    type=float)
parser.add_option('--PtEta'         ,    dest='PtEta'                , help='Pt-eta string path to save root file to EOS',         default='pt5_eta17')

(opt, args) = parser.parse_args()

outDir='%s/%s/%s/%s'%(os.getcwd(),opt.out,opt.datatype,opt.PtEta)
eosDir='/eos/cms%s/%s'%(opt.eosout,opt.datatype)
eosDirIn='/eos/cms%s'%(opt.eosin)
if (opt.run>=0) : outDir='%s/run_%d'%(outDir,opt.run)

os.system('mkdir -p %s'%outDir)

#To access PU files on the grid
#os.environ['X509_USER_PROXY'] = "%s/.gridproxy.pem"%(os.environ['HOME'])
#export X509_USER_PROXY=/afs/cern.ch/user/${USER:0:1}/${USER}/x509up_u${UID} # if you plan to run skims with HTCondor

if (opt.run<opt.firstRun) :
    os.system('voms-proxy-init --valid 168:00')

os.system('voms-proxy-info')

#wrapper
scriptFile = open('%s/runJob.sh'%(outDir), 'w')
scriptFile.write('#!/bin/bash\n')
scriptFile.write('localdir=`pwd`\n')
scriptFile.write('export HOME=%s\n'%(os.environ['HOME']))
scriptFile.write('export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch \n')
scriptFile.write('source $VO_CMS_SW_DIR/cmsset_default.sh \n')
scriptFile.write('cd %s/\n'%(os.getcwd()))
scriptFile.write('eval `scramv1 runtime -sh`\n')
scriptFile.write('cd $localdir\n')

outTag='_%s'%(opt.PtEta)
if (opt.run>=0) : 
    outTag='%s_run%d'%(outTag,opt.run)

if not opt.skipStep1 :
    #scriptFile.write('cmsRun %s/%s/%s maxEvents=%d generatorRandomSeed=%d minpT=%3.3f maxpT=%3.3f minEta=%3.3f maxEta=%3.3f minz=%3.3f\n'%(os.getcwd(),opt.workflow,opt.config1,opt.nevts,opt.randomSeed,opt.minpT,opt.maxpT,opt.minEta,opt.maxEta,opt.minz))
    scriptFile.write('cmsRun %s/%s/%s maxEvents=%d generatorRandomSeed=%d minpT=%3.3f maxpT=%3.3f minEta=%3.3f maxEta=%3.3f minz=%3.3f\n'%(os.getcwd(),opt.workflow,opt.config1,opt.nevts,opt.randomSeed,opt.pT*0.99,opt.pT*1.01,opt.Eta*0.0994,opt.Eta*0.1006,opt.minz))
elif not opt.skipStep2:
    scriptFile.write('eos cp %s/step1%s.root step1.root\n'%(eosDirIn,outTag))

if not opt.skipStep2 :
    scriptFile.write('cmsRun %s/%s/%s\n'%(os.getcwd(),opt.workflow,opt.config2))
elif not opt.skipStep3 :
    scriptFile.write('eos cp %s/step2%s.root step2.root\n'%(eosDirIn,outTag))

if not opt.skipStep3 :
    scriptFile.write('cmsRun %s/%s/%s\n'%(os.getcwd(),opt.workflow,opt.config3))
else:
    scriptFile.write('eos cp %s/step3%s.root step3.root\n'%(eosDirIn,outTag))
    scriptFile.write('cmsRun %s/%s\n'%(os.getcwd(),opt.configTicl))


scriptFile.write('echo "--Local directory is " $localdir >> runJob.log\n')
scriptFile.write('voms-proxy-info >> runJob.log\n')
scriptFile.write('echo home=$HOME >> runJob.log\n')
scriptFile.write('echo path=$PATH >> runJob.log\n')
scriptFile.write('echo ldlibpath=$LD_LIBRARY_PATH >> runJob.log\n')
scriptFile.write('ls -ltrh * >> runJob.log\n')
if len(opt.eosout)>0:
    scriptFile.write('eos mkdir -p %s\n'%eosDir)
    if not opt.skipStep1 and not opt.skipStep2 and not opt.skipStep3:
        scriptFile.write('for idx in 1 2 3; do\n') 
    elif not opt.skipStep2 and not opt.skipStep3:
        scriptFile.write('rm step1.root\n') 
        scriptFile.write('for idx in 2 3; do\n') 
    elif not opt.skipStep3 :
        scriptFile.write('rm step2.root\n') 
        scriptFile.write('for idx in 3; do\n') 
    else :
        scriptFile.write('rm step3.root\n') 
        scriptFile.write('for idx in 3ticl; do\n') 

    #scriptFile.write('for outfile in step${idx} step${idx}_inDQM step${idx}_inMINIAODSIM; do\n')
    scriptFile.write('for outfile in step${idx}; do\n')
    scriptFile.write('eos cp ${outfile}.root %s/${outfile}%s.root\n'%(eosDir,outTag))
    scriptFile.write('if (( "$?" != "0" )); then\n')
    scriptFile.write('echo " --- Problem with copy of file ${outfile}.root to EOS. Keeping locally." >> runJob.log\n')
    scriptFile.write('else\n')
    scriptFile.write('eossize=`eos ls -l %s/${outfile}%s.root | awk \'{print $5}\'`\n'%(eosDir,outTag))
    scriptFile.write('localsize=`ls -l ${outfile}.root | awk \'{print $5}\'`\n')
    scriptFile.write('if [ $eossize != $localsize ]; then\n')
    scriptFile.write('echo " --- Copy of ${outfile} file to eos failed. Localsize = $localsize, eossize = $eossize. Keeping locally..." >> runJob.log\n')
    scriptFile.write('else\n')
    scriptFile.write('echo " --- Size check done: Localsize = $localsize, eossize = $eossize" >> runJob.log\n')
    scriptFile.write('echo " --- File ${outfile}.root successfully copied to EOS: %s/${outfile}%s.root" >> runJob.log\n'%(eosDir,outTag))
    scriptFile.write('rm ${outfile}.root\n')
    scriptFile.write('fi\n')
    scriptFile.write('fi\n')
    scriptFile.write('done\n')
    scriptFile.write('done\n')
scriptFile.write('cp * %s/.\n'%(outDir))
scriptFile.write('echo "All done"\n')
scriptFile.close()

print 'Getting proxy'
subprocess.check_output(['voms-proxy-info','-path'])

proxyPath=os.popen('voms-proxy-info -path')
proxyPath=proxyPath.readline().strip()

#submit
condorFile = open('%s/condorSubmitProd.sub'%(outDir), 'w')
condorFile.write('x509userproxy = $ENV(X509_USER_PROXY)\n')
condorFile.write('use_x509userproxy = True\n')
condorFile.write('universe = vanilla\n')
condorFile.write('+JobFlavour = "nextweek"\n')
condorFile.write('Executable = %s/runJob.sh\n'%outDir)
condorFile.write('Output = %s/condor.out\n'%outDir)
condorFile.write('Error = %s/condor.err\n'%outDir)
condorFile.write('Log = %s/condor.log\n'%outDir)
condorFile.write('Queue 1\n')
condorFile.close()

os.system('chmod u+rwx %s/runJob.sh'%outDir)
if opt.nosubmit : os.system('echo condor_submit %s/condorSubmitProd.sub'%(outDir)) 
else: 
    os.system('echo submitting job %s'%(outDir))
    os.system('condor_submit %s/condorSubmitProd.sub'%(outDir))

