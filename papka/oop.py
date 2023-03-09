"""Створити клас “Прямокутник”, в якому є наступні атрибути “довжина
сторони А”, “ довжина сторони В” та наступні методи: “Повернути довжину
сторони А”, “ Повернути довжину сторони В”, “Повернути площу”, “
Повернути периметр”, “ Повернути тип” (квадрат/прямокутник). Конструктор
класу повинен приймати розміри сторін А та В. Якщо сторони не задані при
створенні класу, то повинен створюватись квадрат зі сторонами А = 1 и В = 1."""

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
