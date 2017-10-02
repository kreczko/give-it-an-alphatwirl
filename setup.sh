#!/bin/bash

EXAMPLES_ROOT="$(dirname "$(readlink -f "$BASH_SOURCE[0]")")"
export EXAMPLES_ROOT
EXTERNALS=${EXAMPLES_ROOT}/external

ALPHATWIRL=${EXTERNALS}/alphatwirl
ALPHATWIRL_INTERFACE=${EXTERNALS}/alphatwirl_interface
LOCAL=${HOME}/.local/lib/python2.7/site-packages

if [[ -z "${NO_CVMFS}" ]]
then
  echo "Using ROOT, GEANT, pandas etc from CVMFS"
  source /cvmfs/sft.cern.ch/lcg/views/LCG_86/x86_64-slc6-gcc49-opt/setup.sh
fi

PYTHONPATH="${ALPHATWIRL_INTERFACE}:${LOCAL}:${PYTHONPATH}"
export PYTHONPATH="${EXAMPLES_ROOT}:${ALPHATWIRL}:${PYTHONPATH}"

pip install --user -r ${EXAMPLES_ROOT}/requirements.txt
