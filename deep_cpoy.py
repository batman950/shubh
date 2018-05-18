xlist=["a",[20,30]]
alist=["a","20"]
import copy
blist=alist[:]
print(blist)
blist[1]=["c"]
print(blist)
print(alist)
ylist=copy.deepcopy(xlist)
print(ylist)
ylist[1]=[20,30,40]
print(ylist)
print("has no effect as=",xlist)