import random

a = []
a_end = int(input("enter length of list:"))
n = int(input("enter range of list member:"))
while len(a) < a_end:
    a.append(random.randint(1, n))

l = [float(i) for i in a if i % 2 == 0]
p = {x : x ** 2 for x in l}
print(a)
print(l)
print(p)




x = [0, 1]
y = [x.append(x[i] + x[i - 1]) for i in range(1, 10)]
print(x)
