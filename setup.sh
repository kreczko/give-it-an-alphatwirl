#!/bin/bash

EXAMPLES_ROOT="$(dirname "$(readlink -f "$BASH_SOURCE[0]")")"
EXTERNALS=${EXAMPLES_ROOT}/external

ALPHATWIRL=${EXTERNALS}/alphatwirl
ALPHATWIRL_INTERFACE=${EXTERNALS}/alphatwirl_interface
LOCAL=${HOME}/.local/lib/python2.7/site-packages

export PYTHONPATH="${ALPHATWIRL}:${ALPHATWIRL_INTERFACE}:${LOCAL}:${PYTHONPATH}"
