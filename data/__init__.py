from __future__ import print_function
import os
import wget


def get_test_data():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    test_data = os.path.join(dir_path, 'data.root')
    if not os.path.exists(test_data):
        print('Could not find test data locally, downloading (~20 MB) ...')
        wget.download(
            url='http://opendata.cern.ch/record/203/files/data.root',
            out=test_data,
        )

    return test_data, 'events'
