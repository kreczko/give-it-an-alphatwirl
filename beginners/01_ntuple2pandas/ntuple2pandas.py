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


tables = [
    Table(
        input_values=('NJet', 'NMuon', 'NElectron', 'Muon_Px', 'Muon_Py'),
    ),
    Table(
        input_values=('NJet', 'NMuon', 'NElectron', 'Muon_Px', 'Muon_Py'),
        # rename columns (optional)
        output_columns=('n_jet', 'n_muon', 'n_electron', 'muon_px', 'muon_py'),
        # store all the muons (additional row per muon)
        indices=(None, None, None, '(*)', '\\1'),
    ),
]

dataframes = tree.scan(tblcfg=tables, max_events=50)

for df in dataframes:
    print df.to_string(index=False)
