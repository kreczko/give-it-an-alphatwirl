#!/usr/bin/env python
from __future__ import print_function
import os
import ROOT
import alphatwirl as at
from alphatwirl_interface import Tree, Table
from alphatwirl_interface.producers import InvariantMass, TransverseMomentum
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

derivedVariables = TransverseMomentum(
    'muon_pt',
    inputs=['Muon_Px', 'Muon_Py'],
)

preselection = Selection(
    dict(
        All=(
            'NMuon[0] == 2',
            'muon_pt[0] > 20',
            'muon_pt[1] > 20',
            'Muon_Iso[0] < 0.1',
            'Muon_Iso[1] < 0.1',
            'Muon_Charge[0] == -1 * Muon_Charge[1]',
        )
    )
)
preselection.set_monitoring_file('output/test.txt')
selection = Selection(
    dict(
        All=(
            'di_muon_mass[0] > 60',
            'di_muon_mass[0] < 120',
        )
    )
)
selection.set_monitoring_file('output/test2.txt')
di_muon_mass = InvariantMass(
    'di_muon_mass',
    ['Muon_E[0]', 'Muon_Px[0]', 'Muon_Py[0]', 'Muon_Pz[0]'],
    ['Muon_E[1]', 'Muon_Px[1]', 'Muon_Py[1]', 'Muon_Pz[1]'],
)
modules = [
    derivedVariables.as_tuple(),
    preselection.as_tuple(),
    di_muon_mass.as_tuple(),
    selection.as_tuple(),
]
# max_events=-1 -> all events
dataframes = tree.scan(tblcfg=tables, max_events=-1, modules=modules)
for df in dataframes:
    # only save dataframes, not selections
    if hasattr(df, 'to_csv'):
        df.to_csv('output/df.csv')
