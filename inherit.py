class father():
    def eyes(self,a):
        self.a=a
        print("eyes gone on father")
class mother():
    def nose(self):
        print("nose gone on mother")

class child(father,mother):
    def name(self):
        print("shubham")

x=child()
x.eyes()
x.nose()
x.name()