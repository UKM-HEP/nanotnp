#!/bin/bash

set -e

NAME=test
#YOURWP=passingMediumWPElectron
YOURWP=passingHLT_IsoMu40_eta2p1

if [ `echo ${PWD} | awk -F "/" '{print $NF}'` != "analysis" ]; then

    echo "please run the script on analysis folder"
    exit
fi

TnP () {

    echo "RUNNING"
    python tnpEGM_fitter.py settings/${1} --flag ${2} --checkBins
    python tnpEGM_fitter.py settings/${1} --flag ${2} --createBins
    python tnpEGM_fitter.py settings/${1} --flag ${2} --createHist
    python tnpEGM_fitter.py settings/${1} --flag ${2} --doFit
    python tnpEGM_fitter.py settings/${1} --flag ${2} --doFit --mcSig --altSig
    python tnpEGM_fitter.py settings/${1} --flag ${2} --doFit --altSig
    python tnpEGM_fitter.py settings/${1} --flag ${2} --doFit --altBkg
    python tnpEGM_fitter.py settings/${1} --flag ${2} --sumUp

}

#
TnP settings_${NAME}.py ${YOURWP}
