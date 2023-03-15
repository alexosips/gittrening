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
#a = Pramokutnik(5,5)
#a.reversa(),a.reversb(),a.plosh(),a.perimeter(),a.type()
class Shluxa:
    def __init__(self,dolorov_v_chas,rozmer_sisok,name):
        self.dolorov_v_chas = dolorov_v_chas
        self.rozmer_sisok = rozmer_sisok
        self.name = name


    def info(self):
        print(f"Шлюха на ім'я {self.name} має {self.rozmer_sisok} розмір сісічок та бере вона {self.dolorov_v_chas}"
              f" доляров в годину")

    def norm_nenorm(self,old):
        if old >=30:
            print("Та ну її нахуй")
        else:print("Ще покатить возраст")

class Sluxa2(Shluxa):
    def __init__(self,dolorov_v_chas,rozmer_sisok,name,rost):
        super().__init__(dolorov_v_chas,rozmer_sisok,name)
        self.rost = rost
    def info(self):
        print(self.rost,self.dolorov_v_chas)

    def norm_nenorm(self,rost,old):
        super().norm_nenorm(old)
        if rost >=170:
            print("Та ну його нахуй шапала")
        else:
            print("Норм піде рост")

shluxa = Shluxa(15,2,"Анжела")
#shluxa.norm_nenorm(29)
sluxa2 = Sluxa2(15,2,"Анжела",125)
sluxa2.info()
sluxa2.norm_nenorm(156,25)