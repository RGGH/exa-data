'''
Parses CSV files
Inserts values into into PostgreSQL : Docker
'''
import glob
import os
import pandas as pd
import db_connect
from typing import Dict, List

from set_constants import get_paths

CSV_DIRECTORY = get_paths()

#CSV_DIRECTORY = '/home/rag/env/exa-data-1/exa-data/data/flattened_csvs'
os.chdir(CSV_DIRECTORY)

def process_csv(csv_file):
    ''' Load 1 CSV and extract each row, and INSERT each row'''

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

        try:

            current_row = entry[i]
            # convert string to dict
            current_row = current_row.strip('\"')
            d = eval(current_row)

            # shorten the initial query length
            dq = d.get('resource')

            # As per init.sql - placeholders to be replaced with selectors #
            # -------------------------------------------------------------#
            type_ = "type"

            entry_ ="entry"

            full_url = d.get('fullUrl')

            resource_ = "resource placeholder"

            resource_type = (dq.get('resourceType'))

            id = (dq.get('id'))

            # DB name = meta
            resource_meta = dq.get('meta','0')
            resource_meta_profile = resource_meta.get('profile')[0] if isinstance(resource_meta, Dict) else "n"
        
            profile = "profile placeholder"

            text_ = "text placholder"

            # DB name = status_
            resource_text_status = dq.get('text','0')
            status_ = resource_text_status.get('status')if isinstance(resource_text_status, Dict) else ''

            # DB name = div
            resource_text_div = dq.get('text','0')
            div_ = resource_text_div.get('div') if isinstance(resource_text_div, Dict) else ''

            # DB name = extension
            resource_extension = dq.get('extension','0')[0]
            extension = resource_extension.get('url') if isinstance(resource_extension, Dict) else ''
        
            # DB name = url
            resource_extension_extension_url = dq.get('extension','0')[0]
            url_ = resource_extension_extension_url.get('extension')[0].get('url') if isinstance(resource_extension_extension_url, List) else ''

            # DB name = valueCoding
            resource_extension_extension_valueCoding = dq.get('extension','0')[0]
            value_coding = resource_extension_extension_valueCoding.get('extension')[0].get('valueCoding') if isinstance(resource_extension_extension_valueCoding, List) else ''

            # Etc Etc...down to #137...


            # break inserts into manageable 
            # group - 1
            dictionary1 ={ 'info-1' : (type_, 
                                    entry_,
                                    full_url, 
                                    resource_,
                                    resource_type, id, 
                                    resource_meta_profile,
                                    profile,text_,
                                    status_,
                                    div_,
                                    )
            }

            for i in dictionary1.values():

                sql1='''insert into patient_info(type_,entry_,fullUrl,
                resource_,resourceType, id, meta, profile_,text_,status_,div) VALUES{};'''.format(i)

                cursor.execute(sql1)

            # group - 2
            dictionary2 ={ 'info-2' : (extension,
                                    url_,
                                    value_coding)
            }

            for i in dictionary2.values():

                sql2='''insert into patient_info(extension, url_,valueCoding) VALUES{};'''.format(i)

                cursor.execute(sql2)



        except (TypeError, AttributeError) as te:
            print(te)

    conn.commit()
    conn.close()

def main():
    '''Import and parse all CSVs'''
    for csv_file in glob.iglob("*.csv"):
        print(f"processing file {csv_file}")
        print("\n===== New file ========\n")
        process_csv(csv_file)


if __name__ == '__main__':
    '''runs all files if main() is uncommented  
    comment it out, and then uncomment the line below to run on just 1 file'''
    main()
    #process_csv('Aaron697_Dickens475_8c95253e-8ee8-9ae8-6d40-021d702dc78e.csv')
