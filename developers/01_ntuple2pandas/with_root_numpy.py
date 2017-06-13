#!/usr/bin/env python
import os
import root_numpy as rnp
import pandas as pd
from data import get_test_data

input_file, tree_name = get_test_data()

branches = ['NJet', 'NMuon', 'NElectron', 'Muon_Px', 'Muon_Py']
arr = rnp.root2array(input_file, tree_name, branches=branches)

df = pd.DataFrame(arr ,columns=branches)
# print first 10 events with >1 muon
print df[df['NMuon'] > 1].head(10).to_string(index=False)
