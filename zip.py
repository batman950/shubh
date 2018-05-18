first = ["sam", "bat", "cat"]
last = ["ranger", "man", "meow"]

names = zip(first, last)
for a, b in names:
    print(a, b)
y = lambda x: x*7
print(y(9))

print(min(first))
print(max(first))
print(sorted(first))
