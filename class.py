class Enemy:
    life = 3

    def attack(self):
        print("ahh")
        self.life -= 1

    def energy(self):
        if self.life <= 0:
            print("enemy dead")
        else:
            print('enemy ALIVE:life left=' + str(self.life))


enemy1 = Enemy()
enemy2 = Enemy()
enemy2.attack()
enemy2.attack()
enemy2.attack()
enemy1.energy()
enemy2.energy()


class dog:
    c = 0

    def __init__(self, b, c):
        self.breed = b
        self.color = c

    def printinfo(self):
        print("\ncolor is %s and breed is %s" % (self.breed, self.color))

d1=dog("black","pug")
d1.printinfo()
