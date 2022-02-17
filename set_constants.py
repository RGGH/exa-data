import configparser  
import os

def set_paths()->str:   
    config = configparser.ConfigParser()
    ini_path = os.path.join(os.getcwd(),'conf.ini')
    config.read(ini_path)

    CSV_DIRECTORY = config.get('PATHS','csv_dir')
    return CSV_DIRECTORY

