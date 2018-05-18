import pickle
d = ['a','b']
f = open("sam.p", "wb")
pickle.dump(d, f)
f.close()
f = open("sam.p", "rb")
d2 = pickle.load(f)
print(d2)
