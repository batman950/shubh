def eligible(a):
    girls_age = (a / 2) + 7
    return girls_age


sam = eligible(40)
kim = eligible(20)
print('sam can DATE girls', sam)
print("kim can DATE girls", kim, "or older")
print ("not")
