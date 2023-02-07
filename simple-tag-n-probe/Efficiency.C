#include "src/compare_efficiency.C"
#include "src/DoFit_new.cpp"
#include "src/get_conditions.cpp"
#include "src/get_efficiency.cpp"
#include "src/change_bin.cpp"
#include "src/make_hist.cpp"
#include "src/McYield.cpp"

void Efficiency()
{
    //We start by declaring the nature of our dataset. (Is the data real or simulated?)
    bool DataIsMC   = false;
    //Which Muon Id do you want to study?
    //string MuonId   = "PassingProbeTrackingMuon";
    string MuonId = "Probe_wp";
    //Which quantity do you want to use?
    string quantity = "pt"; //Pt, Eta or Phi
    
    /*-----------------------------------I N S E R T    C O D E    H E R E-----------------------------------*/
    //double bins[] = {3, 3.4, 4, 4.5, 5, 5.5};
    //int bin_n     = 5;
    double bins[] = {2, 3.4, 4, 4.2, 4.4, 4.7, 5.0, 5.1, 5.2, 5.4, 5.5, 5.6, 5.7, 5.8, 5.9, 6.2, 6.4, 6.6, 6.8, 7.3, 9.5, 13.0, 17.0, 40};
    int bin_n = 23;       //-- BINS USED TO CALCULATE PT
    /*------------------------------------------------------------------------------------------------------*/
    
    //Now we must choose initial conditions in order to fit our data
    double *init_conditions = new double[4];
    /*-----------------------------------I N S E R T    C O D E    H E R E-----------------------------------*/
    init_conditions[0] = 3.1; /*peak1-starting*/
    init_conditions[1] = 2.9; /*peak1-min*/
    init_conditions[2] = 3.2; /*peak2-max*/
    init_conditions[3] = 0.001; /*sigma-starting*/
    init_conditions[4] = 0.01; /*sigma-min*/
    init_conditions[5] = 0.1; /*sigma-max*/
    /*------------------------------------------------------------------------------------------------------*/

    //init_conditions[0] = 3.1; /*peak1-starting*/
    //init_conditions[1] = 3.0; /*peak1-min*/
    //init_conditions[2] = 3.2; /*peak2-max*/
    //init_conditions[3] = 0.001; /*sigma-starting*/
    //init_conditions[4] = 0.01; /*sigma-min*/
    //init_conditions[5] = 0.10; /*sigma-max*/

    /*------------------------------------------------------------------------------------------------------*/
    
    string* conditions = get_conditions(bin_n, bins, "Probe_" + quantity);
    double ** yields_n_errs = new double*[bin_n];
    
    for (int i = 0; i < bin_n; i++)
    {
      cout<<"fitting on bin number : "<< i << endl;
      if (DataIsMC)
	yields_n_errs[i] = McYield(conditions[i], quantity);
      else
	yields_n_errs[i] = doFit_new(conditions[i], MuonId, quantity, init_conditions);
      //doFit returns: [yield_all, yield_pass, err_all, err_pass]
    }
    
    TH1F *yield_ALL  = make_hist("ALL" , yields_n_errs, 0, bin_n, bins, DataIsMC, true);
    TH1F *yield_PASS = make_hist("PASS", yields_n_errs, 1, bin_n, bins, DataIsMC, true);
    
    //----------------------SAVING RESULTS TO Histograms.root--------------------//
    //useful if we require to change the fit on a specific set of bins
    TFile* EfficiencyFile = TFile::Open("Histograms.root","RECREATE");
    yield_ALL->SetDirectory(gDirectory);
    yield_PASS->SetDirectory(gDirectory);
    EfficiencyFile->Write();
    //-----------------------------------------------------------------//
    
    //If all of the fits seem correct we can proceed to generate the efficiency
    TEfficiency* effplot = get_efficiency(yield_ALL, yield_PASS, quantity, DataIsMC);
    
    effplot->Draw();
    effplot->Write();
    EfficiencyFile->Close();
    //In case you want to change the fit on a specific, comment the loop and "result saving" code and uncomment the following function
    //change_bin(/*bin number you want to redo*/, /*condition (you can copy the title from the generated fit .pdf)*/, MuonId, quantity, DataIsMC, init_conditions);
    //bins start on 1
    
    //Once we've calculated the efficiency for both data sets, we can generate
    //a plot that combines both results
    //compare_efficiency(quantity, "Efficiency_Result/" + quantity + "/Efficiency_MC.root", "Efficiency_Result/" + quantity + "/Efficiency_Run2011.root");
}
