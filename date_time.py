from datetime import date

t = date.today()
k = date(2096, 9, 15)
a = k - t
x = k.strftime("%A")
print(t, "    \n", k, " is", x, "\n", "we wil be there in", a, "\n")

from datetime import datetime

d = datetime.now()
print(d)
l = d.strftime("%Y-%B-%I'12-hrs'-%H'24-hrs'-%A-%p-%M'minutes'-%m")  # refer google for more
print(l)

from datetime import timedelta

z = t + timedelta(days=2)
print(z)

datetime.now()
m=p.strftime('%f')
print(m)
for i in range(1000):
    pass
p=datetime.now()
n=p.strftime('%f')
print(int(m)-int(n))