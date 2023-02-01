
# Declare range of the histogram for each variables 
# Each entry in the dictionary contains of the variable name as key and a tuple
# specifying the histogram layout as value. The tuple sets the number of bins,
# the lower edge and the upper edge of the histogram.

zboson_ranges = {
    "Tag_pt"     : [ ( 50 , 0.   , 500 ) , "Tagged XXX p_{T} [GeV/c^{2}]" ],
    "Probe_pt"   : [ ( 50 , 0.   , 500 ) , "Probed XXX p_{T} [GeV/c^{2}]" ] ,
    "Tag_eta"    : [ ( 120 , -3.0 , 3.0 ) , "Tagged XXX #eta" ] ,
    "Probe_eta"  : [ ( 120 , -3.0 , 3.0 ) , "Probed XXX #eta" ] ,
    "pair_mass"  : [ ( 80 , 50   , 130 ) , "Mass (XX) [GeV/c]" ] ,
}

jpsi_ranges = {
"Tag_pt"     : [ ( 50 , 0.   , 500 ) , "Tagged XXX p_{T} [GeV/c^{2}]" ],
    "Probe_pt"   : [ ( 50 , 0.   , 500 ) , "Probed XXX p_{T} [GeV/c^{2}]" ] ,
    "Tag_eta"    : [ ( 120 , -3.0 , 3.0 ) , "Tagged XXX #eta" ] ,
    "Probe_eta"  : [ ( 120 , -3.0 , 3.0 ) , "Probed XXX #eta" ] ,
    "pair_mass"  : [ ( 20 , 2   , 4 ) , "Mass (XX) [GeV/c]" ] ,
}
