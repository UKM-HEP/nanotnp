#!/bin/bash

# -p = particle type: e for electron ; u for muon

python plot.py \
       -n test2012runb_u \
       -l 4.43 \
       -e 8TeV \
       -f 0.6 \
       -p u \
       -r \
       ${PWD}/../../nanoTrimmer/DYJetsToLL_M-50_TuneZ2Star_trimmed/DYJetsToLL_M-50_TuneZ2Star.root \
       ${PWD}/../../nanoTrimmer/Run2012B_SingleMu_trimmed/Run2012B_SingleMu.root


python plot.py \
       -n test2011runb_u \
       -l 2.77 \
       -e 7TeV \
       -f 0.045 \
       -p u \
       -j \
       -r \
       ${PWD}/../../nanoTrimmer/JPsiToMuMu_2MuPEtaFilter_trimmed/JPsiToMuMu_2MuPEtaFilter.root \
       ${PWD}/../../nanoTrimmer/Run2011B_MuOnia_trimmed/Run2011B_MuOnia.root
