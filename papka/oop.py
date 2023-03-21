#english trening
englishlist = []
ukrlist = []
class Hello:
    def __init__(self):
        print("Вас зустрічає скрипт для вивчення слів з англйської мови")
        if len(ukrlist) == 0 and len(englishlist) == 0:
            print("У вас покищо немає жодного слова")
            Hello.add(self)
        else:
            pass
    def add(self):
        english = input("Введіть слово з англиської мови: ")
        ukr = input("Введіть його переклад: ")
        if english != ukr:
            englishlist.append(english)
            ukrlist.append(ukr)
        else:
            print("Спробуйте ще раз")
            Hello.add(self)
    def indo(self):
        pass
hello = Hello()