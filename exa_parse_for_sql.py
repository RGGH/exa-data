'''
Parses CSV files
Inserts values into into PostgreSQL : Docker
'''

import ast
import glob
import os

import pandas as pd

# Set file path for CSVs
from set_constants import set_paths

CSV_DIRECTORY = set_paths()
os.chdir(CSV_DIRECTORY)


def get_csvs(csv_file):
    '''parse the csv file as a nested dictionary and extract the values into variables'''

    dict_from_csv = pd.read_csv(csv_file, header=None, index_col=0).squeeze("columns").to_dict()

    response = dict_from_csv
    entry = response[3][1]
    x = ast.literal_eval(entry)

    # Top Level Keys
    fullUrl = x["fullUrl"]  # no nested keys
    resource = x["resource"]  # has nested keys
    request = x["request"]  # no nested keys


    # Get nested values from dict - resource
    # shorten the query length
    dq = x.get("resource")

    resource_type = dq.get("resourceType")
    resource_id = dq.get("id")
    meta = dq.get("meta")

    identifier = dq.get("identifier")
    identifier_use = dq.get("identifier")[0].get("use")
    identifier_system = dq.get("identifier")[0].get("system")
    identifier_value = dq.get("identifier")[0].get("value")

    status = dq.get("status")

    class_system = dq.get("class").get("system")
    class_code = dq.get("class").get("code")

    type_coding_system = dq.get("type")[0].get("coding")[0].get("system")
    type_coding_code = dq.get("type")[0].get("coding")[0].get("code")
    type_coding_display = dq.get("type")[0].get("coding")[0].get("display")

    type_text = dq.get("type")[0].get("text")

    type_subject = dq.get("subject")
    type_subject_reference = dq.get("subject").get("reference")
    type_subject_display = dq.get("subject").get("display")

    participant_type_coding_system = (
        dq.get("participant")[0].get("type")[0].get("coding")[0].get("system")
    )
    participant_type_coding_code = (
        dq.get("participant")[0].get("type")[0].get("coding")[0].get("code")
    )
    participant_type_coding_display = (
        dq.get("participant")[0].get("type")[0].get("coding")[0].get("display")
    )
    participant_type_coding_text = dq.get("participant")[0].get("type")[0].get("text")

    participant_type_coding_period_start = (
        dq.get("participant")[0].get("period").get("start")
    )
    participant_type_coding_period_end = dq.get("participant")[0].get("period").get("end")

    participant_type_coding_individual_reference = (
        dq.get("participant")[0].get("individual").get("reference")
    )
    participant_type_coding_individual_display = (
        dq.get("participant")[0].get("individual").get("display")
    )

    participant_period_start = dq.get("period").get("start")
    participant_period_end = dq.get("period").get("end")

    participant_location_reference = dq.get("location")[0].get("location").get("reference")
    participant_location_display = dq.get("location")[0].get("location").get("display")

    participant_serviceProvider_reference = dq.get("serviceProvider").get("reference")
    participant_serviceProvider_display = dq.get("serviceProvider").get("display")





def main():
    for csv_file in glob.iglob("*.csv"):
        get_csvs(csv_file)
        
if __name__ == '__main__':
    main()