# Flatten the 1 CSV 
# Reference : https://www.geeksforgeeks.org/convert-nested-json-to-csv-in-python/?ref=rp

import glob
import json
import os

import pandas as pd


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
    
        CSV_DIRECTORY = 'data/flattened_csvs'

        
        try:
            os.makedirs(CSV_DIRECTORY, exist_ok = True)
            print(f"Directory {CSV_DIRECTORY} created successfully")
        except OSError as error:
            print(f"Directory {CSV_DIRECTORY} can not be created")

        os.chdir('data')
        print ("Start conversion")
        for json_file in glob.iglob('*.json'):
            print(json_file)
            if json_file.endswith('.json'):
                print(json_file)
                fname = (os.path.splitext(json_file)[0])
                print (fname)

                # Read the JSON file as python dictionary
                data = read_json(json_file)

                # Normalize the nested python dict
                new_data = normalize_json(data=data)
                print("New dict:", new_data, "\n")

                # Create Pandas dataframe
                dataframe = pd.DataFrame(new_data)

   
                # Write to a CSV file
                dataframe.to_csv("flattened_csvs/" + fname + ".csv")


if __name__ == '__main__':
    main()