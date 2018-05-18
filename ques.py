import json

d1=["Q1:whats an apple?","a:fruit b:veg","Q2:whats an eagle?","a:animal b:bird"]

f = open("quiz.json", "w")
d2 = json.dumps(d1)
data = f.write(d2)
f.close()