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


if __name__=="__main__":
    read_data()