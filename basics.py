mylist = [1]
mytuple = (10, 20, 30, 60, 5, 40)
myset = {'car', 'bike', 'plane'}
secset = {'2 wheels', '4 wheels'}
mydict = {'a': "apple", 'b': "ball", 'c': "cat"}
mydict.update({'d': "dog"})
del mydict['a']
print("dictionary:", mydict, "list:", mylist, "set:", myset, "tuple:", mytuple)
mylist.append(20)
print(mylist)
mylist.extend([10, 30, 40, 50])
print(mylist)
mylist.pop()
print(mylist)
mylist.pop(1)
print(mylist)
mylist.remove(10)
print(mylist)
mylist.sort()
print(mylist)
mylist.reverse()
print(mylist)
print(mylist[0:1])
a = mylist.count(40)
print(a)
print(myset - secset)
print(secset - myset)
print(myset & secset)
print(myset ^ secset)
