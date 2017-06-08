#!/usr/bin/env python
import os
import ROOT
import alphatwirl as at
from alphatwirl_interface import Tree, Table

input_file = 'data.root'
tree_name = 'events'

if not os.path.exists(input_file):
    import wget
    wget.download('http://opendata.cern.ch/record/203/files/data.root')

input_file = ROOT.TFile.Open(input_file)
tree = Tree(input_file.Get(tree_name))

RoundLog = at.binning.RoundLog
Binning = at.binning.Binning
muon_bins = [-1000, -100, -30, -10, 0, 10, 30,  100, 1000]

tables = [
    Table(
        input_values=('Jet_Px',),
        bins=(RoundLog(1, 100), ),
    ),
    Table(
        input_values=('Muon_Px', 'Muon_Py'),
        # same binning for Px and Py
        bins=(Binning(muon_bins), Binning(muon_bins)),
    ),
]

dataframes = tree.summarize(tblcfg=tables)

for df in dataframes:
    print df.to_string(index=False)
