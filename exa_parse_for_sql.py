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

csv_directory = set_paths()
os.chdir(csv_directory)


def get_csvs(csv_file):
    '''parse the csv file as a nested dictionary and extract the values into variables'''

    dict_from_csv = pd.read_csv(csv_file, header=None, index_col=0).squeeze("columns").to_dict()

    response = dict_from_csv
    entry = response[3][1]
    top_level = ast.literal_eval(entry)

    # Top Level Keys
    full_url = top_level["fullUrl"]  # no nested keys
    resource = top_level["resource"]  # has nested keys
    request = top_level["request"]  # no nested keys


    # Get nested values from dict - resource
    # shorten the query length
    dq = top_level.get("resource")

    resource_type = dq.get("resourceType")
    resource_id = dq.get("id")
    meta = dq.get("meta")

    # identifier = dq.get("identifier")
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

    participant_service_provider_reference = dq.get("serviceProvider").get("reference")
    participant_service_provider_display = dq.get("serviceProvider").get("display")

    return {"full_url":full_url,
            "resource":resource,
            "request":request,
            "resource_type":resource_type,
            "resource_id":resource_id,
            "meta":meta,
            "identifier_use":identifier_use,
            "identifier_system":identifier_system,
            "identifier_value":identifier_value,
            "status":status,
            "class_system":class_system,
            "class_code":class_code,
            "type_coding_system":type_coding_system,
            "type_coding_code":type_coding_code,
            "type_coding_display":type_coding_display,
            "type_text":type_text,
            "type_subject_reference":type_subject_reference,
            "type_subject_display":type_subject_display,
            "participant_type_coding_system":participant_type_coding_system,
            "participant_type_coding_code":participant_type_coding_code,
            "participant_type_coding_display":participant_type_coding_display,
            "participant_type_coding_text":participant_type_coding_text,
            "participant_type_coding_period_start":participant_type_coding_period_start,
            "participant_type_coding_period_end":participant_type_coding_period_end,
            "participant_type_coding_individual_reference":participant_type_coding_individual_reference,
            "participant_type_coding_individual_display":participant_type_coding_individual_display,
            "participant_period_start":participant_period_start,
            "participant_period_end":participant_period_end,
            "participant_location_reference":participant_location_reference,
            "participant_location_display":participant_location_display,
            "participant_service_provider_reference":participant_service_provider_reference,
            "participant_service_provider_display":participant_service_provider_display
    }


def main():
    '''main - import and parse all CSVS'''
    for csv_file in glob.iglob("*.csv"):
        print(get_csvs(csv_file))


if __name__ == '__main__':
    '''main driver'''
    main()
