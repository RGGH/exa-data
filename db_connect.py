'''connects to the PostgrSQL database in Docker'''
# pip install psycopg2-binary

import psycopg2

ls = []

'''Make connection using psycopg2 - call from each function'''
def make_conn():

    try:
        conn = psycopg2.connect(host="localhost", database="postgres",
                                user="postgres", password="postgres")

    except Exception as e:
        print(e)
        exit(0)

    return conn

'''read from patient_info table'''
def read_data():
    conn = make_conn()
    if conn is not None:
        print('Connection established to PostgreSQL.')

        # Creating a cursor
        cur = conn.cursor()

        # Getting a query ready.
        cur.execute('select * from patient_info;')

        # we are fetching all the data from the query above.
        get_all_data = cur.fetchall()

        # Print all data
        print(get_all_data)

        # Close connection
        cur.close()
        
    else:
        print('Connection not established to PostgreSQL.')


'''create/add data to patient_info table'''
def add_data(result):

    conn = None
    conn = make_conn()

    try:

        # # create data list to pass to cur.execute
        # data = ()
        # a =list(data)
        # for x in result.keys():
        #     a.append(x)
        # data =tuple(a)
        # len_data = (len(data))

        # create a new cursor
        cur = conn.cursor()

        # change variable to enclosed in single quotes for SQL

        # data 1
        full_url = (""+(result.get('full_url'))+"")
        full_url = (""+full_url+"")
        
        identifier_use = result.get('identifier_use')
        identifier_use = (""+identifier_use+"")
        
        p_status = result.get('p_status')
        p_status = (""+p_status+"")
        
        # data 2 
        class_system = result.get('class_system')
        class_system = (""+class_system+"")

        class_code = result.get('class_code')
        class_code = (""+class_code+"")

        type_coding_system = result.get('type_coding_system')
        type_coding_system = (""+type_coding_system+"")

        type_coding_code = result.get('type_coding_code')
        type_coding_code = (""+type_coding_code+"")

        type_coding_display = result.get('type_coding_display')
        type_coding_display = (""+type_coding_display+"")

        # data 3
        type_text = result.get('type_text')
        type_text = (""+type_text+"")

        type_subject_reference = result.get('type_subject_reference')
        type_subject_reference = (""+type_subject_reference+"")

        type_subject_display = result.get('type_subject_display')
        type_subject_display = (""+type_subject_display+"")

        participant_type_coding_system = result.get('participant_type_coding_system')
        participant_type_coding_system = (""+participant_type_coding_system+"")

        participant_type_coding_code = result.get('participant_type_coding_code')
        participant_type_coding_code = (""+participant_type_coding_code+"")

        participant_type_coding_display = result.get('participant_type_coding_display')
        participant_type_coding_display = (""+participant_type_coding_display+"")

        participant_type_coding_text = result.get('participant_type_coding_text')
        participant_type_coding_text = (""+participant_type_coding_text+"")

        # data 4
        participant_type_coding_period_start = result.get('participant_type_coding_period_start')
        participant_type_coding_period_start = (""+participant_type_coding_period_start+"")

        participant_type_coding_period_end = result.get('participant_type_coding_period_end')
        participant_type_coding_period_end = (""+participant_type_coding_period_end+"")
        
        participant_type_coding_individual_reference = result.get('participant_type_coding_individual_reference')
        participant_type_coding_individual_reference = (""+participant_type_coding_individual_reference+"")
        
        participant_type_coding_individual_display = result.get('participant_type_coding_individual_display')
        participant_type_coding_individual_display = (""+participant_type_coding_individual_display+"")
        
        participant_location_display = result.get('participant_location_display')
        participant_location_display = (""+participant_location_display+"")
                
        participant_service_provider_reference = result.get('participant_service_provider_reference')
        participant_service_provider_reference = (""+participant_service_provider_reference+"")

        participant_service_provider_display = result.get('participant_service_provider_display')
        participant_service_provider_display = (""+participant_service_provider_display+"")

        # SQL INSERT to paitient_info
        SQL1 = "INSERT INTO patient_info (full_url, identifier_use,p_status) VALUES (%s,%s,%s);"
        SQL2 = "INSERT INTO patient_info(class_system,class_code,type_coding_system,type_coding_code,type_coding_display) VALUES (%s,%s,%s,%s,%s);"
        SQL3 = "INSERT INTO patient_info(type_text,type_subject_reference,type_subject_display,participant_type_coding_system,participant_type_coding_code,participant_type_coding_display,participant_type_coding_text) VALUES (%s,%s,%s,%s,%s,%s,%s);"
        SQL4 = "INSERT INTO patient_info(participant_type_coding_period_start,participant_type_coding_period_end,participant_type_coding_individual_reference,participant_type_coding_individual_display,participant_location_display,participant_service_provider_reference,participant_service_provider_display) VALUES (%s,%s,%s,%s,%s,%s,%s);"

        data1 =(full_url,identifier_use,class_system)
        data2 =(class_system,class_code,type_coding_system, type_coding_code,type_coding_display)
        data3 =(type_text,type_subject_reference,type_subject_display,participant_type_coding_system,participant_type_coding_code,participant_type_coding_display,participant_type_coding_text)
        data4 =(participant_type_coding_period_start,participant_type_coding_period_end,participant_type_coding_individual_reference,participant_type_coding_individual_display,participant_location_display,participant_service_provider_reference,participant_service_provider_display)

        cur.execute(SQL1, data1)
        cur.execute(SQL2, data2)
        cur.execute(SQL3, data3)
        cur.execute(SQL4, data4)
    
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()



read_data()