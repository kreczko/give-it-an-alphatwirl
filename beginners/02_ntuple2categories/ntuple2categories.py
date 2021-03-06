#!/usr/bin/env python
import os
import ROOT
import alphatwirl as at
from alphatwirl_interface import Tree, Table
from data import get_test_data

input_file, tree_name = get_test_data()

input_file = ROOT.TFile.Open(input_file)
tree = Tree(input_file.Get(tree_name))

RoundLog = at.binning.RoundLog
Binning = at.binning.Binning
muon_bins = [-1000, -100, -30, -10, 0, 10, 30,  100, 1000]

tables = [
# adding 1D table binned in 'Jet_Px'(logarithmic, rounded bins)
    Table(
        input_values=('Jet_Px',),
        bins=(RoundLog(1, 100), ),
    ),
# adding 2D table binned in Muon_Px and Muon_Py
    Table(
        input_values=('Muon_Px', 'Muon_Py'),
        # same binning for Px and Py
        bins=(Binning(muon_bins), Binning(muon_bins)),
    ),
]

dataframes = tree.summarize(tblcfg=tables)

for df in dataframes:
    print df.to_string(index=False)
