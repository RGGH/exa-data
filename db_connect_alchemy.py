'''connects to the PostgrSQL database in Docker'''
# pip install psycopg2-binary
from ast import Index
from sqlalchemy import create_engine
import psycopg2
import pandas as pd

# establish connections
conn_string = 'postgresql://postgres:postgres@127.0.0.1/postgres'

def add_data(result):
    db = create_engine(conn_string)
    conn = db.connect()
    conn1 = psycopg2.connect(
        database="postgres",
    user='postgres', 
    password='postgres', 
    host='127.0.0.1', 
    port= '5432'
    )

    conn1.autocommit = True
    cursor = conn1.cursor()

    data = pd.DataFrame.from_dict(result)
    data
    # converting data to sql
    data.to_sql('patient_info', conn, if_exists= 'replace')
    
    # fetching all rows
    sql1='''select * from patient_info;'''
    cursor.execute(sql1)
    for i in cursor.fetchall():
        print(i)
    
    conn1.commit()
    conn1.close()