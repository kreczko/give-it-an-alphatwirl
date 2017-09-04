import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('output/df.csv')

fig, ax = plt.subplots()
df.hist('di_muon_mass', ax=ax, bins=100)
fig.savefig('output/di_muon_mass.png')
