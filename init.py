class Enemy:

    def __init__(self,x):
        self.energy = x
    def life(self):
        print(self.energy)

enemy1=Enemy(5)
enemy2=Enemy(15)
enemy1.life()
enemy2.life()
