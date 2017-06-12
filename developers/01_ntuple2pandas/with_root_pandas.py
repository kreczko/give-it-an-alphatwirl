#!/usr/bin/env python
from __future__ import print_function
import os
from root_pandas import read_root

input_file = 'data.root'
tree_name = 'events'

if not os.path.exists(input_file):
    import wget
    wget.download('http://opendata.cern.ch/record/203/files/data.root')

branches = ['NJet', 'NMuon', 'NElectron', 'Muon_Px', 'Muon_Py']


print('*'*50)
print('Arrays in columns')
print('*'*50)
df = read_root(input_file, tree_name, columns=branches)
# print first 10 events with > 1 muons
print(df[df['NMuon'] > 1].head(10).to_string(index=False))

print('*'*50)
print('Flattened data frame')
print('*'*50)
# now with 'flatten' enabled. This will create 1 row per muon
df = read_root(input_file, tree_name, columns=branches, flatten=True)
# print first 10 events with > 1 muons
print(df[df['NMuon'] > 1].head(20).to_string(index=False))
