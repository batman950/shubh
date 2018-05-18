a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
n = int(input("enter a num "))
new_list = []
for i in range(len(a)):
    if a[i] < n:
        new_list.append(i)
print(new_list)