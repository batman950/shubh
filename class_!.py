class Product:
    cat = "drink"
    print(cat)

    def __init__(self, n, r, q, amt=0):
        self.name = n
        self.rate = r
        self.quantity = q
        self.amount = amt

    def showp(self):
        self.amount = self.quantity * self.rate
        print("%s will have %d" % (self.name, self.amount))


p = Product("ram", 20, 2)
p.showp()
