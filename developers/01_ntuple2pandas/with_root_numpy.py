#!/usr/bin/env python
import os
import root_numpy as rnp
import pandas as pd

input_file = 'data.root'
tree_name = 'events'

if not os.path.exists(input_file):
    import wget
    wget.download('http://opendata.cern.ch/record/203/files/data.root')

branches = ['NJet', 'NMuon', 'NElectron', 'Muon_Px', 'Muon_Py']
arr = rnp.root2array(input_file, tree_name, branches=branches)

df = pd.DataFrame(arr ,columns=branches)
# print first 10 events with >1 muon
print df[df['NMuon'] > 1].head(10).to_string(index=False)
