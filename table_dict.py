import json
import sqlite3

my_dict={'1':'apple'}
con = sqlite3.connect('mydata.db')
con.execute("""CREATE TABLE IF NOT EXISTS data1(id INT PRIMARY KEY ,name TEXT)""")
cursor = con.cursor()
cursor.execute("INSERT INTO data1 VALUES(NULL ,:1);",my_dict )
cursor.execute("SELECT * FROM data1")
for i in cursor:
    print(i)
con.close()

