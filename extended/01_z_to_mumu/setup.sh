#!/bin/bash

# use top level setup
source ../../setup.sh

# add specific requirements
if [ -f requirements.txt ]; then
  pip install --user -r requirements.txt
fi

mkdir -p output
