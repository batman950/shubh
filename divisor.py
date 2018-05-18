num = int(input("enter a num to be divided: "))
list = []
for i in range(1, num):
    if num % i == 0:
        list.append(i)
print(list)
