from bs4 import BeautifulSoup
import json

fy = open("sam.txt", "r")
file1 = fy.read()
soup = BeautifulSoup(file1,"html.parser")
tds = soup.findAll('a')
sch=[]
for i in tds:   #to remove the tag from the output
    m=(i.string)
    sch.append(m)
print(sch)




f = open("sam.json", "w")
data = json.dumps(sch)
f.write(data)
f.close()




