#!/usr/bin/env python
from __future__ import print_function
import os
import ROOT
import alphatwirl as at
from alphatwirl_interface import Tree, Table
from alphatwirl_interface.producers import InvariantMass
from alphatwirl_interface import Selection
from data import get_test_data
import numpy as np

input_file, tree_name = get_test_data()
input_file = ROOT.TFile.Open(input_file)
tree = Tree(input_file.Get(tree_name))
tables = [
    Table(
        input_values=(
            'NJet', 'di_muon_mass'),
    ),
]
preselection = Selection(
    dict(
        All=('NMuon[0] == 2')
    )
)
preselection.set_monitoring_file('test.txt')
selection = Selection(
    dict(
        All=(
            'di_muon_mass[0] > 60',
            'di_muon_mass[0] < 120',
        )
    )
)
selection.set_monitoring_file('test2.txt')
di_muon_mass = InvariantMass(
    'di_muon_mass',
    ['Muon_E[0]', 'Muon_Px[0]', 'Muon_Py[0]', 'Muon_Pz[0]'],
    ['Muon_E[1]', 'Muon_Px[1]', 'Muon_Py[1]', 'Muon_Pz[1]'],
)
modules = [
    preselection.as_tuple(),
    di_muon_mass.as_tuple(),
    selection.as_tuple(),
]
dataframes = tree.scan(tblcfg=tables, max_events=1000, modules=modules)
for df in dataframes:
    # only print dataframes, not selectoins
    if hasattr(df, 'to_string'):
        print(df.to_string(index=False))
