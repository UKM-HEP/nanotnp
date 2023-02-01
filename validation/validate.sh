#!/bin/bash

# -p = particle type: e for electron ; u for muon

python plot.py \
       -n 2011runb_u \
       -l 2.77 \
       -e 7TeV \
       -f 0.08 \
       -p u \
       -j \
       -r \
       /home/jovyan/data/trimmed/hazim/JPsiToMuMu_2MuPEtaFilter_trimmed/JPsiToMuMu_2MuPEtaFilter.root \
       /home/jovyan/data/trimmed/hazim/Run2011B_MuOnia_trimmed/Run2011B_MuOnia.root
