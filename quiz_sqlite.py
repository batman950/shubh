import sqlite3
import json

con = sqlite3.connect('mydata.db')
con.execute("""CREATE TABLE IF NOT EXISTS quiz(ques varchar(50),opt varchar(50))""")
cursor = con.cursor()
cursor.execute("""INSERT INTO quiz(ques,opt) VALUES("what is an apple?","a:fruit b:veg")""")
cursor.execute("""INSERT INTO quiz(ques,opt) VALUES("what is an eagle?","a:animal b:bird")""")
cursor.execute("SELECT * FROM quiz")
s = 0
s = int(s)
for i in cursor:
    print(i[0])
    print(i[1])
ans = "a"
opt = input("whats ur answer?")
if opt != ans:
    print("sorry")
else:
    print("correct")
    s = s + 1
print(s)
for i in cursor:
    print(i[2])
    print(i[3])
ans = "b"
opt = input("whats ur answer?")
if opt != ans:
    print("sorry")
else:
   print("correct")
   s = s + 1
print(s)
