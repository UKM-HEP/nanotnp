
double* McYield(string condition, string quant, string MuonID_str = "Probe_wp")
{
  TFile *file0    = TFile::Open("/home/shoh/Works/cmsopendata/trimmed_v1/jenny/JPsiToMuMu_2MuPEtaFilter_trimmed/JPsiToMuMu_2MuPEtaFilter.root");
  //TFile *file0    = TFile::Open("/home/shoh/Works/cmsopendata/trimmed_v1/hazim/JPsiToMuMu_2MuPEtaFilter_trimmed/JPsiToMuMu_2MuPEtaFilter.root");
    TTree *DataTree = (TTree*)file0->Get(("events"));
    
    double _mmin = 2.;  double _mmax = 5.;

    RooRealVar MuonID(MuonID_str.c_str(), MuonID_str.c_str(), 0, 7); //Muon_Id
    
    RooRealVar InvariantMass("pair_mass", "pair_mass", _mmin, _mmax);

    RooRealVar weights("weights","weights", 0. , 10.);
    
    double* limits = new double[2];
    if (quant == "pt") {
        limits[0] = 0;
        limits[1] = 40;
    }
    if (quant == "eta") {
        limits[0] = -3;
        limits[1] = 3;
    }
    if (quant == "phi") {
        limits[0] = -2;
        limits[1] = 2;
    }
    RooRealVar quantity(("Probe_" + quant).c_str(), ("Probe_" + quant).c_str(), limits[0], limits[1]);
    
    RooFormulaVar* redeuce = new RooFormulaVar("PPTM", condition.c_str(), RooArgList(quantity));
    RooDataSet *Data_ALL    = new RooDataSet("DATA", "DATA", DataTree, RooArgSet(InvariantMass, MuonID, quantity, weights), *redeuce, "weights" );

    RooFormulaVar* cutvar = new RooFormulaVar("PPTM", ( condition + " && " + MuonID_str + " == 3").c_str() , RooArgList(MuonID, quantity));
    RooDataSet *Data_PASSING = new RooDataSet("DATA_PASS", "DATA_PASS", DataTree, RooArgSet(InvariantMass, MuonID, quantity, weights), *cutvar, "weights" );
    
    double* output = new double[2];
    output[0] = Data_ALL->sumEntries(); cout<<"Data_ALL->sumEntries() : "<< output[0] <<endl;
    output[1] = Data_PASSING->sumEntries(); cout<<"Data_PASSING->sumEntries() : "<< output[1] <<endl;
    return output;
}

