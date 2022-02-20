'''
Connects to the PostgrSQL database in Docker
this used by exa_parse_for_sql, but can be used
on its own to check the database contents
'''
# pip install psycopg2-binary

import psycopg2
import set_constants


'''Make connection using psycopg2 - call from each function'''
def make_conn():

    # creds = set_constants.get_db_creds()
    # host = creds[0]
    # user= creds[1]
    # password=creds[2]
    # database = creds[3]
    
    try:
        conn = psycopg2.connect(host='localhost', database='postgres',
                                user='postgres', password='postgres')

    except Exception as e:
        print(e)
        exit(0)

    return conn

def read_data():
    '''read all from patient_info table'''
    conn = make_conn()
    if conn is not None:
        print('Connection established to PostgreSQL.')

        # Creating a cursor
        cur = conn.cursor()

        # Getting a query ready.
        cur.execute('select * from patient_info ORDER BY 8 DESC;')

        # we are fetching all the data from the query above.
        get_all_data = cur.fetchall()

        # Print all data
        print(get_all_data)

        # Close connection
        cur.close()
        
    else:
        print('Connection not established to PostgreSQL.')


def read_div():
    '''read div data from patient_info table'''
    conn = make_conn()
    if conn is not None:
        print('Connection established to PostgreSQL.')

        # Creating a cursor
        cur = conn.cursor()

        # Getting a query ready.
        cur.execute("select fullUrl from patient_info WHERE resourceType != 'Patient';")

        # we are fetching all the data from the query above.
        get_all_data = cur.fetchall()

        # Print all data
        print(get_all_data)

        # Close connection
        cur.close()
        
    else:
        print('Connection not established to PostgreSQL.')

if __name__=="__main__":
    '''reads patient_info table'''
    read_div()