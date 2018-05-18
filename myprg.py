import product
p1=product.Product("apple", 20, 10)
p2=product.Product("mango", 20, 13)
p3=product.Product("orange", 20, 11)
my_stock=[p1,p2,p3]
#print(my_stock)

x=[]
for p in my_stock:
    #print(p.pname)
    #print(p.price)
    #print(p.qty)
    m = []
    m.extend([p.pname,p.price,p.qty])
    x.append(m)

print(x)
