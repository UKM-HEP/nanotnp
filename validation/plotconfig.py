
# Declare range of the histogram for each variables 
# Each entry in the dictionary contains of the variable name as key and a tuple
# specifying the histogram layout as value. The tuple sets the number of bins,
# the lower edge and the upper edge of the histogram.

zboson_ranges = {
    "Tag_pt"     : [ ( 80 , 0.   , 400 ) , "Tagged XXX p_{T} [GeV/c^{2}]" ],
    "Probe_pt"   : [ ( 80 , 0.   , 400 ) , "Probed XXX p_{T} [GeV/c^{2}]" ] ,
    "Tag_eta"    : [ ( 10 , -3.0 , 3.0 ) , "Tagged XXX #eta" ] ,
    "Probe_eta"  : [ ( 10 , -3.0 , 3.0 ) , "Probed XXX #eta" ] ,
    "pair_mass"  : [ ( 30 , 60   , 120 ) , "Mass (XX) [GeV/c]" ] ,
}

jpsi_ranges = {
    "Tag_pt"     : [ ( 40 , 0.   , 200 ) , "Tagged XXX p_{T} [GeV/c^{2}]" ],
    "Probe_pt"   : [ ( 40 , 0.   , 200 ) , "Probed XXX p_{T} [GeV/c^{2}]" ] ,
    "Tag_eta"    : [ ( 10 , -3.0 , 3.0 ) , "Tagged XXX #eta" ] ,
    "Probe_eta"  : [ ( 10 , -3.0 , 3.0 ) , "Probed XXX #eta" ] ,
    "pair_mass"  : [ ( 20 , 2   , 4 ) , "Mass (XX) [GeV/c]" ] ,
}
