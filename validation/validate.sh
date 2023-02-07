#!/bin/bash

set -e

#baseDir=/home/jovyan/data
#baseDir=/disk01/cms-open-data
baseDir=/home/shoh/Works/cmsopendata

# amirul, electron
python plot.py \
       -n 2012runa_e \
       -l 0.89 \
       -e 8TeV \
       -p e \
       -r \
       ${baseDir}/trimmed_v1/amirul/DYJetsToLL_M-50_TuneZ2Star_trimmed/DYJetsToLL_M-50_TuneZ2Star.root \
       ${baseDir}/trimmed_v1/amirul/Run2012A_SingleElectron_trimmed/Run2012A_SingleElectron.root

# mohan, muon
python plot.py \
       -n 2012runa_u \
       -l 0.89 \
       -e 8TeV \
       -p u \
       -r \
       ${baseDir}/trimmed_v1/mohan/DYJetsToLL_M-50_TuneZ2Star_trimmed/DYJetsToLL_M-50_TuneZ2Star.root \
       ${baseDir}/trimmed_v1/mohan/Run2012A_SingleMu_trimmed/Run2012A_SingleMu.root

# zainol, muon
python plot.py \
       -n 2012runb_u \
       -l 4.43 \
       -e 8TeV \
       -p u \
       -r \
       ${baseDir}/trimmed_v1/zainol/DYJetsToLL_M-50_TuneZ2Star_trimmed/DYJetsToLL_M-50_TuneZ2Star.root \
       ${baseDir}/trimmed_v1/zainol/Run2012B_SingleMu_trimmed/Run2012B_SingleMu.root

# jenny, muon
python plot.py \
       -n 2011runa_u \
       -l 2.33 \
       -e 7TeV \
       -f 0.92 \
       -p u \
       -j \
       -r \
       ${baseDir}/trimmed_v1/jenny/JPsiToMuMu_2MuPEtaFilter_trimmed/JPsiToMuMu_2MuPEtaFilter.root \
       ${baseDir}/trimmed_v1/jenny/Run2011A_MuOnia_trimmed/Run2011A_MuOnia.root

# hazim, muon
python plot.py \
       -n 2011runb_u \
       -l 2.77 \
       -e 7TeV \
       -f 0.06 \
       -p u \
       -j \
       -r \
       ${baseDir}/trimmed_v1/hazim/JPsiToMuMu_2MuPEtaFilter_trimmed/JPsiToMuMu_2MuPEtaFilter.root \
       ${baseDir}/trimmed_v1/hazim/Run2011B_MuOnia_trimmed/Run2011B_MuOnia.root
