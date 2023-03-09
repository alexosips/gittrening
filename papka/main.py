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

    def divssion(self):
        for i in range(len(self.list)):
            f = self.list[i]
            f = f / 2
            self.list[i] = f
        print(f"Числа поділені на 2: {self.list}") #Діляться з відсортованого списка

    def number_in_list(self):
        for i in range(len(self.list)):
            if self.list[i] == 10:

                print('Належить списку')
            else:

                print("не належить списку")

    def kul_1_plus_9(self):
        print(f"Перший елемент списка:{self.list[1]}")
        print(f"Дев'ятий елемент списка:{self.list[9]}")
        print(f"Сумма першого елемента та дев'ятого:{self.list[1] + self.list[9]}")

    def half(self):
        pass#Поділити список на дві половини та вивести


start = Start()
start.print()
start.arrange()
start.revers()
start.divssion()
#start.number_in_list()
start.kul_1_plus_9()
#на забуть визвать функцію