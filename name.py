class boy:
    gender = "male"

    def __init__(self, x):  # calls itself
        self.name = x

r = boy("sam")
p = boy("bat")

print(r.gender)
print(p.gender)
print(r.name)
print(p.name)