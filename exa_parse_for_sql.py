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
CSV_DIRECTORY = '/home/rag/env/exa-data-1/exa-data/data/flattened_csvs'
os.chdir(CSV_DIRECTORY)

def process_csv(csv_file):

    df = pd.read_csv(csv_file)
    num_rows = len(df)

    print(f"this file has {num_rows} rows")

    '''parse the csv file as a nested dictionary and extract the values into variables'''
    dict_from_csv = pd.read_csv(csv_file, header=None, index_col=0).squeeze("columns").to_dict()

    response = dict_from_csv
    entry = response[3]

    conn = db_connect.make_conn()
    conn.autocommit = True
    cursor = conn.cursor()

    # iterate though each row, get values from dict, and INSERT into TABLE patient_info
    for i in range(0,num_rows):

        current_row = entry[i]
        # convert string to dict
        current_row = current_row.strip('\"')
        d = eval(current_row)

       # shorten the query length
        dq = d.get('resource')

        # As per init.sql
        type_ = "type"
        entry_ ="entry"
        full_url = "furl"
        resource_ = "pres"
        resource_type = (dq.get('resourceType'))
        id = (dq.get('id'))
        meta = (dq.get('meta'))

        dictionary ={ 'info-1' : (type_, entry_,
                                full_url, resource_,
                                resource_type, id, 'meta')
        }

        for i in dictionary.values():
            sql1='''insert into patient_info(type_,entry_,fullUrl,
            resource_,resourceType, id, meta) VALUES{};'''.format(i)

            cursor.execute(sql1)

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
    main()
    #process_csv('Gus973_Windler79_09e292d4-f186-331c-ed95-c503acabc54e.csv')
