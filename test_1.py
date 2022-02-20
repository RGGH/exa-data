'''pytest'''

import set_constants
import pytest

def test_path():
    '''Verify the output of `calc_addition` function'''
    output = set_constants.get_paths()
    assert output == 'data/flattened_csvs'
    
class DatabaseHelper():
    '''Test DB Connection'''
    
    def __init__(self,creds):

        self.host = creds[0]
        self.dbname = creds[3]
        self.user = creds[1]
        self.password = creds[2]

    @pytest.fixture(scope='session')
    def test_creds():
        creds = set_constants.get_db_creds()
        db = DatabaseHelper(creds)
        assert db == True

creds = set_constants.get_db_creds()
db = DatabaseHelper(creds)





    







