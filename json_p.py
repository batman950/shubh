import json
d = {"a": 100, "b": 200}
print(d)
f = open("sam.json", "w")
data = json.dumps(d)
f.write(data)
f.close()
f = open("sam.json", "r")
data = f.read()
d2 = json.loads(data)
print(d2)

