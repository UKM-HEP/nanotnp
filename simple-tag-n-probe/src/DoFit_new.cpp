using namespace RooFit;

double* doFit_new(string condition, string MuonID_str, string quant, double* init_conditions, bool save = true) // RETURNS ARRAY WITH [yield_all, yield_pass, err_all, err_pass]    ->   OUTPUT ARRAY
{
    TFile *file0    = TFile::Open("/Users/shoh/Works/trimmed_v1/jenny/Run2011A_MuOnia_trimmed/Run2011A_MuOnia.root");
    TTree *DataTree = (TTree*)file0->Get(("events"));
    
    double _mmin = 2.4;  double _mmax = 4.;
    
    // Testing the flag
    RooRealVar MuonID(MuonID_str.c_str(), MuonID_str.c_str(), 0, 7); //Muon_Id

    // Create observables   
    RooRealVar InvariantMass("pair_mass", "pair_mass", _mmin, _mmax);
    
    double* limits = new double[2];
    if (quant == "pt") {
        limits[0] = 0.;
        limits[1] = 40.;
    }
    if (quant == "eta") {
        limits[0] = -3.;
        limits[1] = 3.;
    }
    if (quant == "phi") {
        limits[0] = -2.;
        limits[1] = 2.;
    }

    RooRealVar quantity(("Probe_" + quant).c_str(), ("Probe_" + quant).c_str(), limits[0], limits[1]);
    
    RooFormulaVar* redeuce = new RooFormulaVar("PPTM", condition.c_str(), RooArgList(quantity));
    RooDataSet *Data_ALL    = new RooDataSet("DATA", "DATA", DataTree, RooArgSet(InvariantMass, MuonID, quantity),*redeuce);

    RooFormulaVar* cutvar = new RooFormulaVar("PPTM", (condition + " && " + MuonID_str + " == 3").c_str() , RooArgList(MuonID, quantity));
    RooDataSet *Data_PASSING = new RooDataSet("DATA_PASS", "DATA_PASS", DataTree, RooArgSet(InvariantMass, MuonID, quantity), *cutvar);
    
    RooDataHist* dh_ALL     = Data_ALL->binnedClone();
    RooDataHist* dh_PASSING = Data_PASSING->binnedClone();
    
    // Construct signal pdf                                                                                                                                                                                  
    RooRealVar mean("mean", "mean", init_conditions[0], init_conditions[1], init_conditions[2]);
    RooRealVar sigma("sigma", "sigma", init_conditions[3], init_conditions[4], init_conditions[5]);
    RooGaussian gx("gx", "gx", InvariantMass, mean, sigma);

    // Construct background pdf                                                                                                                                                                              
    RooRealVar a0("a0", "a0", -0.1, -1, 1);
    RooRealVar a1("a1", "a1", 0.004, -1, 1);
    RooChebychev px("px", "px", InvariantMass, RooArgSet(a0, a1));

    // prepare ALL and PASS signal and background.
    double n_signal_initial_total =(Data_ALL->sumEntries(TString::Format("abs(pair_mass-%g)<0.015",init_conditions[0]))-Data_ALL->sumEntries(TString::Format("abs(pair_mass-%g)<0.030&&abs(pair_mass-%g)>.015",init_conditions[0],init_conditions[0]))) / Data_ALL->sumEntries();
    double n_back_initial = 1. - n_signal_initial_total;

    RooRealVar n_signal_total("n_signal_total","n_signal_total",n_signal_initial_total,0.,Data_ALL->sumEntries());
    RooRealVar n_signal_total_pass("n_signal_total_pass","n_signal_total_pass",n_signal_initial_total,0.,Data_PASSING->sumEntries());
    
    RooRealVar n_back("n_back","n_back",n_back_initial,0.,Data_ALL->sumEntries());
    RooRealVar n_back_pass("n_back_pass","n_back_pass",n_back_initial,0.,Data_PASSING->sumEntries());


    // Construct composite pdf for ALL and PASS PDF   
    RooAddPdf* model;
    RooAddPdf* model_pass;
    
    model      = new RooAddPdf("model","model", RooArgList(gx, px),RooArgList(n_signal_total, n_back));
    model_pass = new RooAddPdf("model_pass", "model_pass", RooArgList(gx, px),RooArgList(n_signal_total_pass, n_back_pass));


    cout<<"Running simultaneous fit now"<< endl;
    /////////////////////////////////////////////////////////////////
    // SIMULTANEOUS FIT
    RooCategory sample("sample","sample") ;
    sample.defineType("All") ;
    sample.defineType("PASSING") ;

    // Construct combined dataset in (x,sample)
    //RooDataSet combData("combData", "combined data", x, Index(sample), Import({{"ALL", *dh_ALL}, {"PASSING", *dh_PASSING}}));
    //RooDataHist combData("combData", "combined data", InvariantMass, Index(sample), Import({{"ALL", *dh_ALL}, {"PASSING", *dh_PASSING}}));
    
    RooDataHist combData("combData","combined data",InvariantMass,Index(sample),Import("ALL",*dh_ALL),Import("PASSING",*dh_PASSING));

    // Construct a simultaneous pdf using category sample as index:
    // associate model with the physics state and model_ctl with the control state
    //RooSimultaneous simPdf("simPdf", "simultaneous pdf", {{"physics", &model}, {"control", &model_ctl}}, sample);
    
    RooSimultaneous simPdf("simPdf","simultaneous pdf",sample);
    
    simPdf.addPdf(*model,"ALL");
    simPdf.addPdf(*model_pass,"PASSING");
    
    std::unique_ptr<RooFitResult> fitres{simPdf.fitTo(combData, PrintLevel(-1), Save())};
    fitres->Print();

    
    // OUTPUT ARRAY
    double* output = new double[4];
    
    RooRealVar* yield_ALL = (RooRealVar*) fitres->floatParsFinal().find("n_signal_total");
    RooRealVar* yield_PASS = (RooRealVar*) fitres->floatParsFinal().find("n_signal_total_pass");
    
    output[0] = yield_ALL->getVal(); cout<<"yield_ALL->getVal() : "<< output[0] <<endl;
    output[1] = yield_PASS->getVal(); cout<<"yield_PASS->getVal() : "<< output[1] <<endl;
    
    output[2] = yield_ALL->getError();
    output[3] = yield_PASS->getError();

    RooPlot *frame = InvariantMass.frame(RooFit::Title("Invariant Mass"));
    RooPlot *frame_pass = InvariantMass.frame(RooFit::Title("Invariant Mass"));

    TCanvas* c_all  = new TCanvas;
    TCanvas* c_pass = new TCanvas;

    c_all->cd();
    
    frame->SetTitle( ("ALL_" + condition).c_str() );
    frame->SetXTitle("#mu^{+}#mu^{-} invariant mass [GeV/c^{2}]");
    Data_ALL->plotOn(frame,Name("data_all"));
    
    model->plotOn(frame,Name("sig_bkg"),RooFit::LineStyle(kSolid),RooFit::LineColor(kBlue));
    model->plotOn(frame,Name("sig_only"),RooFit::Components("gx"),RooFit::LineStyle(kDashed),RooFit::LineColor(kGreen));
    model->plotOn(frame,Name("bkg_only"),RooFit::Components("px"),RooFit::LineStyle(kDashed),RooFit::LineColor(kRed));

    frame->Draw("");

    TLegend *leg1 = new TLegend(0.65,0.73,0.86,0.87);
    leg1->SetFillColor(kWhite);
    leg1->SetLineColor(kWhite);
    leg1->AddEntry("data","Data", "P");
    leg1->AddEntry("sig_bkg","Signal + background","LP");
    leg1->AddEntry("bkg_only","Background only", "LP");
    leg1->AddEntry("sig_only","Signal only", "LP");
    leg1->Draw();
    
    // passframe

    c_pass->cd();
    
    frame_pass->SetTitle( ("PASSING_" + condition).c_str() );
    frame_pass->SetXTitle("#mu^{+}#mu^{-} invariant mass [GeV/c^{2}]");
    Data_PASSING->plotOn(frame_pass,Name("data_passing"));
    
    model_pass->plotOn(frame_pass,Name("sig_bkg"),RooFit::LineStyle(kSolid),RooFit::LineColor(kBlue));
    model_pass->plotOn(frame_pass,Name("sig_only"),RooFit::Components("gx"),RooFit::LineStyle(kDashed),RooFit::LineColor(kGreen));
    model_pass->plotOn(frame_pass,Name("bkg_only"),RooFit::Components("px"),RooFit::LineStyle(kDashed),RooFit::LineColor(kRed));
    
    frame_pass->Draw();

    TLegend *leg2 = new TLegend(0.65,0.73,0.86,0.87);
    leg2->SetFillColor(kWhite);
    leg2->SetLineColor(kWhite);
    leg2->AddEntry("data","Data", "P");
    leg2->AddEntry("sig_bkg","Signal + background","LP");
    leg2->AddEntry("bkg_only","Background only", "LP");
    leg2->AddEntry("sig_only","Signal only", "LP");
    leg2->Draw();

    if(save)
    {
        c_pass->SaveAs(("Fit_Result/" + condition + "_PASS.pdf").c_str());
        c_all->SaveAs (("Fit_Result/" + condition + "_ALL.pdf").c_str());
    }
        
    // DELETING ALLOCATED MEMORY
    delete[] limits;
    //
    delete file0;
    //
    delete Data_ALL;
    delete Data_PASSING;
    //
    delete dh_ALL;
    delete dh_PASSING;
    //
    delete cutvar;
    delete redeuce;
    //
    delete c_all;
    delete c_pass;
    //
    delete model;
    delete model_pass;
    //delete fitres;
    
    return output;
}
