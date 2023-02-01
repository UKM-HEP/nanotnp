from libPython.tnpClassUtils import tnpSample
import os
cwd = os.getcwd()
opendataDir = '%s/../../nanoTrimmer/' % cwd

datasets = {
    
    # 2011 7TeV muon
    'Run2011A_MuOnia' : tnpSample('Run2011A_MuOnia', opendataDir + 'Run2011A_MuOnia_trimmed/Run2011A_MuOnia.root', lumi = 2.33 ),
    'Run2011B_MuOnia' :	tnpSample('Run2011B_MuOnia', opendataDir + 'Run2011B_MuOnia_trimmed/Run2011B_MuOnia.root', lumi = 2.77 ),
    'JPsiToMuMu_2MuPEtaFilter' : tnpSample('JPsiToMuMu_2MuPEtaFilter', opendataDir + 'JPsiToMuMu_2MuPEtaFilter_trimmed/JPsiToMuMu_2MuPEtaFilter.root', isMC = True, nEvts = -1 ),
    
    # 2012 8TeV Electron
    'Run2012A_SingleElectron' :	tnpSample('Run2012A_SingleElectron', opendataDir + 'Run2012A_SingleElectron_trimmed/Run2012A_SingleElectron.root', lumi = 0.89 ),
    
    # 2012 8TeV Muon
    'Run2012A_SingleMu' : tnpSample('Run2012A_SingleMu', opendataDir + 'Run2012A_SingleMu_trimmed/Run2012A_SingleMu.root', lumi = 0.89 ),
    'Run2012B_SingleMu' : tnpSample('Run2012B_SingleMu', opendataDir + 'Run2012B_SingleMu_trimmed/Run2012B_SingleMu.root', lumi = 4.43 ),

    # 2012 9TeV monte carlo
    'DYJetsToLL_M-50_TuneZ2Star' : tnpSample('DYJetsToLL_M-50_TuneZ2Star', opendataDir + 'DYJetsToLL_M-50_TuneZ2Star_trimmed/DYJetsToLL_M-50_TuneZ2Star.root', isMC = True, nEvts = -1 )
}

testDir = '/home/shoh/Work/cmsopendata/nanotnp/'
tests = {
    'Run2012B_SingleMu' : tnpSample('Run2012B_SingleMu', testDir + 'Run2012B_SingleMu.root' , lumi = 4.43 ),
    'DYJetsToLL_M-50_TuneZ2Star' : tnpSample('DYJetsToLL_M-50_TuneZ2Star', testDir + 'DYJetsToLL_M-50_TuneZ2Star.root', isMC = True, nEvts = -1 , weight=8. )
}
