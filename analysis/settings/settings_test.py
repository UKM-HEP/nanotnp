import os
#############################################################
########## General settings
#############################################################
# Name of your study
name = "run2012b_u_test"

# flag to be Tested
flags = {
    'passingMediumWPElectron'   : 'Probe_wp == 3',
    'passingSoftWPMuon'         : 'Probe_wp == 3',
    'passingHLT_IsoMu40_eta2p1' : 'HLT_IsoMu40_eta2p1 == 1'
}

# output destination
baseOutDir = '%s/results/tnpEleID_%s' %( os.getcwd() , name )

#############################################################
########## samples definition  - preparing the samples
#############################################################
### samples are defined in etc/inputs/tnpSampleDef.py
### not: you can setup another sampleDef File in inputs
import etc.inputs.tnpOpenData as tnpSamples
tnpTreeDir = 'events'

samplesDef = {
    'data'   : tnpSamples.tests['Run2012B_SingleMu'].clone(),
    'mcNom'  : tnpSamples.tests['DYJetsToLL_M-50_TuneZ2Star'].clone(),
    'mcAlt'  : tnpSamples.tests['DYJetsToLL_M-50_TuneZ2Star'].clone(),
    'tagSel' : tnpSamples.tests['DYJetsToLL_M-50_TuneZ2Star'].clone(),
}

## some sample-based cuts... general cuts defined here after
## require mcTruth on MC DY samples and additional cuts
## all the samples MUST have different names (i.e. sample.name must be different for all)
## if you need to use 2 times the same sample, then rename the second one
#samplesDef['data'  ].set_cut('run >= 273726')
samplesDef['data'].set_tnpTree(tnpTreeDir)
if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_tnpTree(tnpTreeDir)
if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_tnpTree(tnpTreeDir)
if not samplesDef['tagSel'] is None: samplesDef['tagSel'].set_tnpTree(tnpTreeDir)

if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_mcTruth()
if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_mcTruth()
if not samplesDef['tagSel'] is None: samplesDef['tagSel'].set_mcTruth()
if not samplesDef['tagSel'] is None:
    samplesDef['tagSel'].rename('mcAltSel_DYJetsToLL_M-50_TuneZ2Star')
    samplesDef['tagSel'].set_cut('Tag_pt > 37') #canceled non trig MVA cut

## set MC weight, simple way (use tree weight) 
weightName = 'weights'
if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_weight(weightName)
if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_weight(weightName)
if not samplesDef['tagSel'] is None: samplesDef['tagSel'].set_weight(weightName)

#############################################################
########## bining definition  [can be nD bining]
#############################################################
biningDef = [
    { 'var' : 'Probe_eta' , 'type': 'float', 'bins': [ -2.5 , -2.0 , -1.566 , -1.442 , -0.8 , 0.0 , 0.8 , 1.442 , 1.566 , 2.0 , 2.5 ] },
    #{ 'var' : 'Probe_pt' , 'type': 'float', 'bins': [ 10 , 15 , 20 , 35 , 50 , 90 , 150 , 500 ] },
    #{ 'var' : 'Probe_eta' , 'type': 'float', 'bins': [ -2.0 , -1.4 , -0.8 , 0.0 , 0.8 , 1.4 , 2.0 ] },
    { 'var' : 'Probe_pt' , 'type': 'float', 'bins': [ 25 , 35 , 50 , 90 , 150 ] },
]

#############################################################
########## Cuts definition for all samples
#############################################################
### cut
cutBase   = 'Tag_pt > 32 && abs(Tag_eta) < 2.17 && Tag_pdgId+Probe_pdgId == 0'

# can add addtionnal cuts for some bins (first check bin number using tnpEGM --checkBins)
#additionalCuts = { 
#    0 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*Tag_pt*(1-cos(event_met_pfphi-Tag_phi))) < 45',
#    1 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*Tag_pt*(1-cos(event_met_pfphi-Tag_phi))) < 45',
#    2 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*Tag_pt*(1-cos(event_met_pfphi-Tag_phi))) < 45',
#    3 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*Tag_pt*(1-cos(event_met_pfphi-Tag_phi))) < 45',
#    4 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*Tag_pt*(1-cos(event_met_pfphi-Tag_phi))) < 45',
#    5 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*Tag_pt*(1-cos(event_met_pfphi-Tag_phi))) < 45',
#    6 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*Tag_pt*(1-cos(event_met_pfphi-Tag_phi))) < 45',
#    7 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*Tag_pt*(1-cos(event_met_pfphi-Tag_phi))) < 45',
#    8 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*Tag_pt*(1-cos(event_met_pfphi-Tag_phi))) < 45',
#    9 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*Tag_pt*(1-cos(event_met_pfphi-Tag_phi))) < 45',
#    10 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*Tag_pt*(1-cos(event_met_pfphi-Tag_phi))) < 45',
#    11 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*Tag_pt*(1-cos(event_met_pfphi-Tag_phi))) < 45',
#    12 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*Tag_pt*(1-cos(event_met_pfphi-Tag_phi))) < 45',
#    13 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*Tag_pt*(1-cos(event_met_pfphi-Tag_phi))) < 45',
#    14 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*Tag_pt*(1-cos(event_met_pfphi-Tag_phi))) < 45',
#    15 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*Tag_pt*(1-cos(event_met_pfphi-Tag_phi))) < 45',
#    16 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*Tag_pt*(1-cos(event_met_pfphi-Tag_phi))) < 45',
#    17 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*Tag_pt*(1-cos(event_met_pfphi-Tag_phi))) < 45',
#    18 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*Tag_pt*(1-cos(event_met_pfphi-Tag_phi))) < 45',
#    19 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*Tag_pt*(1-cos(event_met_pfphi-Tag_phi))) < 45',
#}

#### or remove any additional cut (default)
additionalCuts = None

#############################################################
########## fitting params to tune fit by hand if necessary
#############################################################
tnpParNomFit = [
    "meanP[-0.0,-5.0,5.0]","sigmaP[0.9,0.5,5.0]",
    "meanF[-0.0,-5.0,5.0]","sigmaF[0.9,0.5,5.0]",
    "acmsP[60.,50.,80.]","betaP[0.05,0.01,0.08]","gammaP[0.1, -2, 2]","peakP[90.0]",
    "acmsF[60.,50.,80.]","betaF[0.05,0.01,0.08]","gammaF[0.1, -2, 2]","peakF[90.0]",
    ]

tnpParAltSigFit = [
    "meanP[-0.0,-5.0,5.0]","sigmaP[1,0.7,6.0]","alphaP[2.0,1.2,3.5]" ,'nP[3,-5,5]',"sigmaP_2[1.5,0.5,6.0]","sosP[1,0.5,5.0]",
    "meanF[-0.0,-5.0,5.0]","sigmaF[2,0.7,15.0]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[2.0,0.5,6.0]","sosF[1,0.5,5.0]",
    "acmsP[60.,50.,75.]","betaP[0.04,0.01,0.06]","gammaP[0.1, 0.005, 1]","peakP[90.0]",
    "acmsF[60.,50.,75.]","betaF[0.04,0.01,0.06]","gammaF[0.1, 0.005, 1]","peakF[90.0]",
    ]
     
tnpParAltBkgFit = [
    "meanP[-0.0,-5.0,5.0]","sigmaP[0.9,0.5,5.0]",
    "meanF[-0.0,-5.0,5.0]","sigmaF[0.9,0.5,5.0]",
    "alphaP[0.,-5.,5.]",
    "alphaF[0.,-5.,5.]",
    ]
        
