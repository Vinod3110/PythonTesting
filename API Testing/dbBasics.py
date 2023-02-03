import mysql.connector
from utilities.configurations import *
# conn = mysql.connector.connect(host='localhost', database='APIDevelop',
#                                user='root', password='root')
# print(conn.is_connected())
# cursor = conn.cursor()
# cursor.execute('select * from CustomerInfo')
# row = cursor.fetchone()         ##-- It will fecth only one row
# print(row)                      ##-- Result will be in tuple format - ()
# rowAll = cursor.fetchall()      ##-- It will fetch the all the remaining rows of result expect the first fecth one result
# print(rowAll)                   ##-- Result will be in the List, tuple format [(),(),...]

# rows = cursor.fetchall()
# print(rows)
# final_sum = 0
# for row in rows:
#     final_sum = final_sum + row[2]
#
# print(final_sum)
## -- Update the information in table using python

# query = "update customerInfo set Location = %s where CourseName = %s"
# data = ('UK','Jmeter')
# cursor.execute(query,data)
# conn.commit()

## -- Delete the information in table using python
# query = 'delete from customerInfo where %s = %s'
# data = ('courseName', 'WebServices')
#
# cursor.execute(query, data)
# conn.commit()
# cursor.execute('select * from CustomerInfo')
# updatedRows = cursor.fetchall()
# conn.close()

## Executing DB connection from Global files

conn = getConnection()
print(conn.is_connected())
cursor = conn.cursor()
cursor.execute('select * from CustomerInfo')
rows = cursor.fetchall()
print(rows)
final_sum = 0
for row in rows:
    final_sum = final_sum + row[2]
print(final_sum)
assert final_sum == 361