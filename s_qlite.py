import sqlite3
import json

con = sqlite3.connect('mydata.db')
con.execute("""CREATE TABLE IF NOT EXISTS quiz(ques varchar(50),opt varchar(50))""")
cursor = con.cursor()
cursor.execute("""INSERT INTO quiz(ques,opt) VALUES("what is an apple?","a:fruit b:veg"),("what is an eagle?","a:animal b:bird")""")

cursor.execute("SELECT * FROM quiz")
a=[]
for i in cursor:
    b=[]
    b.extend([i])
    a.append(b)

f = open("table.json", "w")

data = json.dumps(a)
f.write(data)
f.close()
con.close()