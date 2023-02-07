set -e

#baseDir=/home/jovyan/data
#baseDir=/disk01/cms-open-data
baseDir=/home/shoh/Works/cmsopendata

# test
python plot.py \
       -n test2012runa_e \
       -l 0.89 \
       -e 8TeV \
       -f 1. \
       -p e \
       -r \
       ${baseDir}/trimmed_v1/amirul/DYJetsToLL_M-50_TuneZ2Star_trimmed/DYJetsToLL_M-50_TuneZ2Star.root \
       ${baseDir}/trimmed_v1/amirul/Run2012A_SingleElectron_trimmed/Run2012A_SingleElectron.root
