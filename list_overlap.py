import random
n = int(input("enter a number: "))  # to decide the range of list
a = []
a_end = int(input("enter length of a: "))
b = []
b_end = int(input("enter length of b: "))
c = []    # take the list c for usage
while len(a) < a_end:
    k = random.randint(0, n)
    if k not in a:
        a.append(k)
print(a)
while len(b) < b_end:
    k = random.randint(0, n)
    if k not in b:
        b.append(k)
print(b)
if len(b) > len(a):
    for i in b:
        if i in a and i not in c:
            c.append(i)
else:
    for i in a:
        if i in b and i not in c:
            c.append(i)
print(c)
