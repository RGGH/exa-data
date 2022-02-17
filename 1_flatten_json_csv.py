'''
Flattens all JSON files to CSV
!pip install pandas
'''

import glob
import json
import os
import configparser

import pandas as pd

config = configparser.ConfigParser()
ini_path = os.path.join(os.getcwd(),'conf.ini')
config.read(ini_path)

CSV_DIRECTORY = config.get('PATHS','csv_dir')


def read_json(filename: str) -> dict:

    try:
        with open(filename, "r") as f:
            data = json.loads(f.read())
    except:
        raise Exception(f"Reading {filename} file encountered an error")

    return data


def normalize_json(data: dict) -> dict:

    new_data = dict()
    for key, value in data.items():
        if not isinstance(value, dict):
            new_data[key] = value
        else:
            for k, v in value.items():
                new_data[key + "_" + k] = v

    return new_data


def main():
    '''create output directory, read JSON, flatten, output to CSV
    iterates through files which have *.json extension
    '''

    try:
        os.makedirs(CSV_DIRECTORY, exist_ok=True)
        print(f"Directory {CSV_DIRECTORY} created successfully")
    except OSError as error:
        print(f"Directory {CSV_DIRECTORY} can not be created")

    os.chdir('data')
    print("Start conversion")
    for json_file in glob.iglob('*.json'):

        if json_file.endswith('.json'):

            # Create filename minus extension
            fname = (os.path.splitext(json_file)[0])

            # Read the JSON file as a Python dictionary
            data = read_json(json_file)

            new_data = normalize_json(data=data)
            #print("New dict:", new_data, "\n")
            print(f"converting {fname}")

            dataframe = pd.DataFrame(new_data)
            dataframe.to_csv("flattened_csvs/" + fname + ".csv")

    print("\ncomplete, converted csv files are in 'data/flattened_csvs'\n")


if __name__ == '__main__':
    main()
