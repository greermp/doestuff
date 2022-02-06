import pymysql.cursors
import csv

conn = pymysql.connect(host='localhost',
                   user='mgreer',
                   database='ProductivIT')


cur = conn.cursor()

with open ('test_query.sql', 'r') as file:
    query = file.read()
    
cur.execute(query)

# print(cur.fetchall())

out_file = "test.csv"
num_fields = len(cur.description)
print(num_fields)
field_names = [i[0] for i in cur.description]
print(field_names)

with open(out_file, 'w') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(field_names)
    for row in cur.fetchall():
        print(row)
        writer.writerow(row)
        
cur.close()