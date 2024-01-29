import sqlite3
import pandas as pd

conn = sqlite3.connect('STAFF.db')

table_name = 'INSTRUCTOR'
attribute_list = ['ID', 'FNAME', 'LNAME', 'CITY', 'CCODE']

file_path = '/home/project/INSTRUCTOR.csv'
df = pd.read_csv(file_path, names = attribute_list)

df.to_sql(table_name, conn, if_exists = 'replace', index = False)
print('Table is ready')

query = f"SELECT * FROM {table_name}"
output = pd.read_sql(query, conn)
print(query)
print(output)

query = f"SELECT FNAME FROM {table_name}"
output = pd.read_sql(query, conn)
print(query)
print(output)

query = f"SELECT COUNT(*) FROM {table_name}"
output = pd.read_sql(query, conn)
print(query)
print(output)

data_dict = {'ID' : [100],
            'FNAME' : ['John'],
            'LNAME' : ['Doe'],
            'CITY' : ['Paris'],
            'CCODE' : ['FR']}
data_append = pd.DataFrame(data_dict)

data_append.to_sql(table_name, conn, if_exists = 'append', index = False)
print('Data appended successfully')

query = f"SELECT COUNT(*) FROM {table_name}"
output = pd.read_sql(query, conn)
print(query)
print(output)

conn.close()
