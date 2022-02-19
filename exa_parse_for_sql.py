'''
Parses CSV files
Inserts values into into PostgreSQL : Docker
'''
import glob
import os
import db_connect 
import pandas as pd

# # Set file path for CSVs
# from set_constants import set_paths
csv_directory = '/home/rag/env/exa-data-1/exa-data/data/flattened_csvs'
os.chdir(csv_directory)

def process_csv(csv_file):

    df = pd.read_csv(csv_file)
    num_rows = len(df)

    print(f"this file has {num_rows} rows")

    '''parse the csv file as a nested dictionary and extract the values into variables'''
    dict_from_csv = pd.read_csv(csv_file, header=None, index_col=0).squeeze("columns").to_dict()

    response = dict_from_csv
    entry = response[3]


    # iterate though each row, get values from dict, and INSERT into TABLE patient_info
    for i in range(0,num_rows):

        current_row = entry[i]
        # convert string to dict
        current_row = current_row.strip('\"')
        d = eval(current_row)

       # shorten the query length
        dq = d.get('resource')

        # As per init.sql

        full_url = ""
        p_resource = ""
        request = ""
        resource_type = (dq.get('resourceType'))
        resource_id = (dq.get('id'))

        meta_profile = (dq.get('meta'))

        identifier_use = (dq.get('identifier')[0].get('use'))
        identifier_system = (dq.get('identifier')[0].get('system'))
        identifier_value = (dq.get('identifier')[0].get('value'))

        status = (dq.get('class'))
        print(status)

        class_system = (dq.get('class').get('system'))
        # class_code = (dq.get('class').get('code'))
        # type_coding_system = (dq.get('type')[0].get('coding')[0].get('system'))
        # type_coding_code = (dq.get('type')[0].get('coding')[0].get('code'))
        # type_coding_display = (dq.get('type')[0].get('coding')[0].get('display'))
        # type_text = (dq.get('type')[0].get('text'))
        # type_subject = (dq.get('subject'))
        # type_subject_reference = (dq.get('subject').get('reference'))
        # type_subject_display = (dq.get('subject').get('display'))
        # type_subject_display
        # participant_type_coding = (dq.get('participant')[0].get('type')[0].get('coding'))
        # participant_type_coding_system = (dq.get('participant')[0].get('type')[0].get('coding')[0].get('system'))
        # participant_type_coding_code=(dq.get('participant')[0].get('type')[0].get('coding')[0].get('code'))
        # participant_type_coding_display=(dq.get('participant')[0].get('type')[0].get('coding')[0].get('display'))
        # participant_type_coding_text=(dq.get('participant')[0].get('type')[0].get('text'))
        # participant_type_coding_text
        # participant_type_coding_period=(dq.get('participant')[0].get('period'))
        # participant_type_coding_period_start=(dq.get('participant')[0].get('period').get('start'))
        # participant_type_coding_period_start
        # participant_type_coding_period_end=(dq.get('participant')[0].get('period').get('end'))
        # participant_type_coding_period_end
        # participant_type_coding_individual=(dq.get('participant')[0].get('individual'))
        # participant_type_coding_individual_reference = (dq.get('participant')[0].get('individual').get('reference'))
        # participant_type_coding_individual_display = (dq.get('participant')[0].get('individual').get('display'))
        # participant_type_coding_individual_display
        # participant_period=(dq.get('period').get('end'))
        # participant_location=(dq.get('location')[0].get('location'))
        # participant_location_reference = (dq.get('location')[0].get('location').get('reference'))
        # participant_location_display = (dq.get('location')[0].get('location').get('display'))
        # participant_serviceProvider_reference = (dq.get('serviceProvider').get('reference'))
        # participant_serviceProvider_display = (dq.get('serviceProvider').get('display'))








        # DATABASE #    

        conn = db_connect.make_conn()

        conn.autocommit = True
        cursor = conn.cursor()

        dictionary ={ 'info-1' : (full_url, resource_type,
                                p_resource, resource_id,
                                meta_profile, identifier_use, identifier_system )
        }

        for i in dictionary.values():
            sql2='''insert into patient_info(full_url ,
                p_resource, request, resource_type, resource_id, meta, 
                identifier_use,identifier_system) VALUES{};'''.format(i)

            cursor.execute(sql2)

        conn.commit()
        conn.close()

def main():
    '''Import and parse all CSVs'''
    for csv_file in glob.iglob("*.csv"):
        print(f"processing file {csv_file}")
        print("\n===== New file ========\n")
        process_csv(csv_file)


if __name__ == '__main__':
    '''main driver'''
    #main()
    process_csv('Gus973_Windler79_09e292d4-f186-331c-ed95-c503acabc54e.csv')
