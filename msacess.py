from pandas import DataFrame
import numpy as np

import pyodbc
from sqlalchemy import create_engine

db_file = r'E:\MY COMPUTER\Desktop\Python\DcmeBE.mdb'
#user = 'user'
#password = 'pw'

conn = pyodbc.connect(odbc_conn_str)

cur = conn.cursor()


qry = cur.execute("SELECT * FROM table WHERE INST = '796116'")
dataf = DataFrame(qry.fetchall()) 
print(dataf)

