class emp:
    c = 1  # class variable(can be accessed by any one within the class)

    def __init__(self, n, a ): # __init__ is constructor  # object method
        self.name = n # object variable
        self.address = a
        emp.c += 1


class manager(emp):
    def __init__(self, n, a, s):
        self.salary = s
        emp.__init__(self, n, a) # calling super class constructor

    def printinfo(self):
        print("name of manager is :%s\t,his address is :%s\t and salary is :%d\t count is:%d" % (
            self.name, self.address, self.salary, emp.c))

    @classmethod  # creating class method
    def printcount(self):
        print(emp.c)


m = manager("s", "ranchi", 2321321)
m.printinfo()
manager.printcount()
