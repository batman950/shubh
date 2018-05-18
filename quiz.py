import json


print("demo quiz")
name = input("please enter ur name:\n")
print("get ready quiz begins shortly\n"
      "heres the first question\n")

f = open("quiz.json", "r")
data = f.read()
d2 = json.loads(data)
s = 0
s = int(s)
print(d2[0],"\n")
print(d2[1],"\n")
ans = "a"
opt = input("whats ur answer?please enter options:")
if opt != ans:
    print("sorry ur answer is wrong\n")
else:
    print("correct\n")
    s = s + 1
print("your score 0ut of 10:",s,"\n","moving to next\n")
print(d2[2],"\n")
print(d2[3],"\n")
ans = "b"
opt = input("whats ur answer?please enter options:")
if opt != ans:
    print("sorry ur answer is wrong\n")
else:
    print("correct\n")
    s = s + 1
print("your score 0ut of 10:",s,"\n","moving to next\n")
print("ur final score is",s)