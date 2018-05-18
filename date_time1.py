from datetime import datetime
p=datetime.now()
print(p)
m=p.strftime('%f')
print(m)
for i in range(100):
    pass
    
p1=datetime.now()
print(p1)
n=p1.strftime('%f')
print(n)
print(int(n)-int(m))
