'''Set filepaths'''
import configparser
import os


def set_paths() -> str:
    '''Set CSV Path in the ini file'''
    config = configparser.ConfigParser()
    ini_path = os.path.join(os.getcwd(), 'conf.ini')
    config.read(ini_path)

    csv_directory = config.get('PATHS', 'csv_dir')
    return csv_directory
