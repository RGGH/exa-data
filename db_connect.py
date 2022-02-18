'''connects to the PostgrSQL database in Docker'''
# pip install psycopg2-binary

import psycopg2

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

    # Convert the Dictionary into a List of Tuples for SQL 
    data = list(result.items())
    print(data)

    try:

        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        for d in data:
            cur.execute("insert into patient_info(full_url, identifier_use,p_status,class_system ) VALUES (%s,%s,%s,%s)",d)

    
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