"""Створити клас “Прямокутник”, в якому є наступні атрибути “довжина
сторони А”, “ довжина сторони В” та наступні методи: “Повернути довжину
сторони А”, “ Повернути довжину сторони В”, “Повернути площу”, “
Повернути периметр”, “ Повернути тип” (квадрат/прямокутник). Конструктор
класу повинен приймати розміри сторін А та В. Якщо сторони не задані при
створенні класу, то повинен створюватись квадрат зі сторонами А = 1 и В = 1."""
"""
class Car:

    def __init__(self, name, volume, color):
        self.name = name
        self.volome = volume
        self.color = color

    def info(self):
        print(f"Name: {self.name}\nVolome: {self.volome}\nColor: {self.color}")

class Yourcar(Car):
    def plus(self):
        print(f"Suma: {self.volome + self.volome}")



class Error:
    def error(self):
        try:
            print(self.name)
        except AttributeError:
            print("Окунь, це не можливо")

car = Car("bmw", 2.5 , "red")
car.info()
ycar = Yourcar("bmw", 2.5 , "red")
ycar.plus()

er = Error()
er.error()

"""
class Kp3:
    def __init__(self):
        string1 = "Я люблю Україну Слава України Слава"
        string2 = "Київ столиця України Cлава Слава"
        self.words1 = string1.split(' ')
        self.words2 = string2.split(' ')
        print(self.words1)
        print(self.words2)
    def rozglat(self):
        print("\nВаріант B\n")
        for i in range(len(self.words1)):
            if self.words1[i] in self.words2:
                print(f"Слово '{self.words1[i]}' знайдено")
            else:
                print(f"Слово '{self.words1[i]}' не знайдено")
    def norozglat(self):
        list = []
        print("\nВаріант А\n")
        for i in range(len(self.words1)):
            if self.words1[i] in self.words2:
                list.append(self.words1[i])
                if list.count(self.words1[i]) >1 :
                    print(f"Слово '{self.words1[i]}' вже було")
                else:
                    print(f"Слово '{self.words1[i]}' знайдено")
            else:
                print(f"Слово '{self.words1[i]}' не знайдено")

kp3 = Kp3()
kp3.rozglat()
kp3.norozglat()