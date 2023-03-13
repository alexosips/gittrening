"""Створити клас “Прямокутник”, в якому є наступні атрибути “довжина
сторони А”, “ довжина сторони В” та наступні методи: “Повернути довжину
сторони А”, “ Повернути довжину сторони В”, “Повернути площу”, “
Повернути периметр”, “ Повернути тип” (квадрат/прямокутник). Конструктор
класу повинен приймати розміри сторін А та В. Якщо сторони не задані при
створенні класу, то повинен створюватись квадрат зі сторонами А = 1 и В = 1."""

class Pramokutnik:
    def __init__(self,stora=1,storb=1 ):
        self.stora = stora
        self.storb = storb

    def reversa(self):
       print(self.stora)

    def reversb(self):
       print(self.storb)

    def plosh(self):
        print(f"площа: {self.stora} * {self.storb}={self.stora*self.storb}")

    def perimeter(self):
        print(f"периметр: {self.stora} + {self.storb} = {self.stora+self.storb}")


    def type(self):
        if self.storb==self.stora:
            print("квадрат")
        else:
            print("прямокутник")
a = Pramokutnik(5,5)
a.reversa()
a.reversb()
a.plosh()
a.perimeter()
a.type()