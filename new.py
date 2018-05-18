list2=[]
for i in range(2,501):
    for k in range(2,i):
       if i%k == 0:
            break
       else:
            list1=[]
            list1.extend([i])
            list2.append(list1)
print(list2)
