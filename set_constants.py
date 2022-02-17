'''Set filepaths'''
import configparser  
import os

'''Set CSV Path in the ini file'''
def set_paths()->str:   
    config = configparser.ConfigParser()
    ini_path = os.path.join(os.getcwd(),'conf.ini')
    config.read(ini_path)

    csv_directory = config.get('PATHS','csv_dir')
    return csv_directory
