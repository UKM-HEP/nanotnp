# Implementation of the plotting step of the analysis
# The plotting combines the histograms to plots which allow us to study the
# initial dataset based on observables motivated through physics.

import argparse, os, sys
import ROOT
import numpy as np
from ROOT import array
from utilities import *

from plotconfig import *

ROOT.gROOT.SetBatch(True)
ROOT.ROOT.EnableImplicitMT(10)
ROOT.TH1.SetDefaultSumw2()
ROOT.gStyle.SetOptStat(0)

# Declare range of the histogram for each variables
# Each entry in the dictionary contains of the variable name as key and a tuple
# specifying the histogram layout as value. The tuple sets the number of bins,
# the lower edge and the upper edge of the histogram.

### RDataframe
# Book a histogram for a specific variable
def bookHistogram( df , variable , range_ , factor=None ):
    match="mcTrue*weights" #*tag_TightHWW_SF*probe_TightHWW_SF"
    cut="1==1" #"Tag_pt > 32 && abs(Tag_eta) < 2.17 && Tag_pdgId+Probe_pdgId == 0"
    probe="1==1"
    flag="1==1"
    
    WEIGHT = match + "*" + factor if factor is not None else "1."
    
    return df.Define( "plotweights" , WEIGHT )\
        .Filter( "1==1" , "Nominal cut" )\
        .Filter( flag , "passing flag" )\
        .Filter( probe , "probe low eta high pt cut" )\
        .Histo1D( ROOT.ROOT.RDF.TH1DModel(variable, variable, range_[0], range_[1], range_[2]), variable, "plotweights" )
pass

# Loop over all variable names and make a plot for each
if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument( '-n' , '--name' , type=str , help='DATA Name' )
    parser.add_argument( '-l' , '--lumi' , type=str , help='total luminosity' )
    parser.add_argument( '-f' , '--factor' , type=str , help='factor in fraction', default="1" )
    parser.add_argument( '-e' , '--energy' , type=str , help='center of mass energy' )
    parser.add_argument( '-p' , '--particle' , type=str , help='particle type' )
    parser.add_argument( '-j', '--jpsi', action='store_true', default=False)
    parser.add_argument( '-r' , '--rootfiles' , type=str , nargs='+', help='path/root file', required=True )

    args = parser.parse_args()
    Name_ = args.name
    Lumi_ = args.lumi
    Factor_ = args.factor
    Energy_ = args.energy
    Particle_ = "e^{+}e^{-}" if args.particle == "e" else "#mu^{+}#mu^{-}"
    ranges = jpsi_ranges if args.jpsi else zboson_ranges
    file_ = args.rootfiles
    Mc_ = list(filter( lambda x : 'DY' in x.split('/')[-1] , file_ )) if not args.jpsi else list(filter( lambda x : 'JPsiToMuMu' in x.split('/')[-1] , file_ ))
    Data_ = list( set(file_) - set(Mc_) )

    print( 'NAME     : ', Name_ )
    print( 'Lumi     : ', Lumi_ )
    print( 'Factor   : ', Factor_ )
    print( 'Energy   : ', Energy_ )
    print( 'Particle : ', Particle_ )
    print( 'DATA     : ', Data_ )
    print( 'MC       : ', Mc_   )

    # apply selection, book histogram
    outpath = './results/%s' %Name_
    if not os.path.isdir(outpath): os.system( 'mkdir -p %s' %outpath )
    # root file consist of variables for each sample
    tfile = ROOT.TFile( "%s/histo_%s.root" %( outpath , Name_ ) , "RECREATE" )

    variables = ranges.keys()
    hists={}
    
    # Process skimmed datasets and produce histograms of variables
    # Process MC
    for imc in Mc_:
        mcName = imc.split('/')[-1].split('.root')[0]
        print(" --> MC samples : %s" %( mcName ) )

        # Load skimmed dataset and apply baseline selection (if any)
        df = ROOT.ROOT.RDataFrame( 'events' , imc )
        # Book histogram
        for variable in variables: hists[variable] = bookHistogram( df , variable , ranges[variable][0] , Factor_ )

        # Write histograms to output file
        for variable in variables: hists[variable].SetName( "{}_{}".format( mcName , variable ) ); hists[variable].Write()

    hists.clear()

    print(" --> DATA : %s" %Name_ )
    # Process Data
    ddf = ROOT.ROOT.RDataFrame( 'events' , Data_ )
    # Book histogram
    for variable in variables: hists[variable] = bookHistogram( ddf , variable , ranges[variable][0] )
    # Write histograms to output file
    for variable in variables: hists[variable].SetName( "{}_{}".format( Name_ , variable ) ); hists[variable].Write()
    
    # plot!
    for imc in Mc_:
        mcName = imc.split('/')[-1].split('.root')[0]
        out_ = '%s/%s' %( outpath , mcName )
        if not os.path.isdir(out_): os.system( 'mkdir -p %s' %out_ )
        print( "using mc sample : " , imc )
        for variable in variables:
            hist_mc = getHistogram( tfile , "{}_{}".format( mcName , variable ) )
            hist_data = getHistogram( tfile , "{}_{}".format( Name_ , variable ) )
            #hdata , hmc , output , variable , xlabel , ylabel , scale , ratio=0 , logy=False , com="7TeV" ):
            pervalue = (ranges[variable][0][2] - ranges[variable][0][1])/ranges[variable][0][0]
            if variable == "pair_mass":
                ranges[variable][1] = ranges[variable][1].replace('XX', Particle_)
            else:
                ranges[variable][1] = ranges[variable][1].replace('XXX', "Electron" if Particle_ == "e^{+}e^{-}" else "Muon" )
                
            histo1D(
                hist_data ,
                hist_mc ,
                out_ ,
                variable ,
                ranges[variable][1] ,
                "Events / %.2f GeV" %( pervalue ) if 'eta' in variable else "Events / %.0f GeV" %( pervalue ) ,
                Lumi_ ,
                4 ,
                False if 'eta' in variable else True ,
                Energy_ ,
                Particle_
            )

    tfile.Close()
