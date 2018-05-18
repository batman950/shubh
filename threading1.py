import threading
class messenger(threading.Thread):
    def run(self):
        for _ in range(10):
            print(threading.currentThread.getname)

x = messenger(name="send")
y = messenger(name="receive")

x.start()
y.start()