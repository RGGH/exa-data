'''pytest'''

import set_constants

def test_path():
    '''Verify the output of `calc_addition` function'''
    output = set_constants.set_paths()
    assert output == 'data/flattened_csvs'

