import random


class Start:
    global list

    def __init__(self):
        self.list = []
        for i in range(0, 10):
            self.list.append(random.randint(1, 40))
    def print(self):
        print(self.list)

    def arrange(self):
       self.list.sort()
       print(self.list)

    def revers(self):
        pass #написати від більшого до меншого

start = Start()
start.print()
start.arrange()
#на забуть визвать функцію