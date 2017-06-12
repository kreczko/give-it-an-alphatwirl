#!/bin/bash

echo "Using ROOT, GEANT, pandas etc from CVMFS"
source /cvmfs/sft.cern.ch/lcg/views/LCG_85/x86_64-slc6-gcc49-opt/setup.sh

pip install --user -r requirements.txt

# use top level setup
source ../../setup.sh
