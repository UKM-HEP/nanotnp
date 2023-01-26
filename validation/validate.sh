#!/bin/bash

# 41.48
python plot.py -n 2012runb_ele -l 41.48 -r \
       ${PWD}/../../nanoTrimmer/DYJetsToLL_M-50_TuneZ2Star_trimmed/DYJetsToLL_M-50_TuneZ2Star.root \
       ${PWD}/../../nanoTrimmer/Run2012B_SingleElectron_trimmed/Run2012B_SingleElectron.root
