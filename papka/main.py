import random


class Start:
    global list

    def __init__(self):
        self.list = []
        for i in range(0, 10):
            self.list.append(random.randint(1, 40))
    def print(self):
        print(f"Вивод списка: {self.list}")

    def arrange(self):
       self.list.sort()
       print(f"Від меншого до більшого: {self.list}")

    def revers(self):
       self.list.reverse ()
       print(f"Від більшого до меншого: {self.list}")


start = Start()
start.print()
start.arrange()
start.revers()
#на забуть визвать функцію