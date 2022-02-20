'''Get filepaths'''
import configparser
import os


def get_paths() -> str:
    '''Set CSV Path from the ini file'''
    config = configparser.ConfigParser()
    ini_path = os.path.join(os.getcwd(), 'conf.ini')
    config.read(ini_path)

    csv_directory = config.get('PATHS', 'csv_dir')
    return csv_directory


def get_db_creds():
    config = configparser.ConfigParser()
    config.read('conf.ini')
    host = config['postgres']['host']
    user = config['postgres']['user']
    passwd = config['postgres']['passwd']
    db = config['postgres']['db']
    return host, user, passwd, db

