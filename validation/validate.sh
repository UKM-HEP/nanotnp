#!/bin/bash

# -p = particle type: e for electron ; u for muon
python plot.py \
       -n 2012runb_ele \
       -l 4.43 \
       -e 8TeV \
       -f 10. \
       -p e \
       -r \
       ${PWD}/../../nanoTrimmer/DYJetsToLL_M-50_TuneZ2Star_trimmed/DYJetsToLL_M-50_TuneZ2Star.root \
       ${PWD}/../../nanoTrimmer/Run2012A_SingleElectron_trimmed/Run2012A_SingleElectron.root
