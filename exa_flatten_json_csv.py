'''
Flattens all source JSON files to CSV
!pip install pandas
Proceed to parse for SQL afterwards
'''

import glob
import json
import os

import pandas as pd

from set_constants import get_paths

CSV_DIRECTORY = get_paths()

def read_json(filename: str) -> dict:
    '''Load the JSON and flatted mulitilayer nesting'''

    try:
        with open(filename, "r") as json_file:
            data = json.loads(json_file.read())
    except:
        raise Exception(f"Reading {filename} file encountered an error")

    return data


def normalize_json(data: dict) -> dict:
    '''flatten nested strucure'''
    new_data = {}
    for key, value in data.items():
        if not isinstance(value, dict):
            new_data[key] = value
        else:
            for k2, v2 in value.items():
                new_data[key + "_" + k2] = v2

    return new_data


def main():
    """create output directory, read JSON, flatten, output to CSV
    iterates through files which have *.json extension
    """

    try:
        os.makedirs(CSV_DIRECTORY, exist_ok=True)
        print(f"Directory {CSV_DIRECTORY} created successfully")
    except OSError as error:
        print(f"Directory {CSV_DIRECTORY} can not be created: ",error)

    os.chdir("data")
    print("Start conversion")
    for json_file in glob.iglob("*.json"):

        if json_file.endswith(".json"):

            # Create filename minus extension
            fname = os.path.splitext(json_file)[0]

            # Read the JSON file as a Python dictionary
            data = read_json(json_file)

            new_data = normalize_json(data=data)
            # print("New dict:", new_data, "\n")
            print(f"converting {fname}")

            dataframe = pd.DataFrame(new_data)
            dataframe.to_csv("flattened_csvs/" + fname + ".csv")

    print("\ncomplete, converted csv files are in 'data/flattened_csvs'\n")


if __name__ == "__main__":
    main()
