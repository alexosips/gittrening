# english trening
class Hello:
    def __init__(self):
        print("\nВас зустрічає скрипт для вивчення слів з англйської мови")
        self.englishlist = ''  # пусті стрінги які перетворяться в списки
        self.ukrlist = ''
        if len(self.printukr()) == 0 and len(self.printenglish()) == 0:  # Перевірка на наявність елементів у файлах
            print("У вас покищо немає жодного слова")
            Hello.add(self)  # У разі пустих файлів запускаєм функцію по додаванню слів
            # Hello.print(self)
        else:
            number = input(  # Інакше запускаємо одну з вибраних дій
                "1-> Показать всі слова англ\n"
                "2-> Показать всі слова укр\n"
                "3-> Додати нове слово\n"
                "4-> Видалити всі слова\n"
                "Введіть число: ")
            if number == "1":
                print(self.printenglish())  # Функція виводу інгліш слів
                Hello()
            elif number == "2":
                print(self.ukrlist)  # Функція виводу укр слів
                Hello()
            elif number == "3":
                self.add()  # Функція додавання слів
            elif number == "4":
                self.delateall()  # Функція видалення всіх слів
                Hello()
            else:
                Hello()

    def add(self):
        self.printenglish()
        self.printukr()
        if len(self.englishlist) == len(self.ukrlist):

            english = input("Введіть слово з англиської мови: ")  # Вводимо потрібні нам слова
            ukr = input("Введіть його переклад: ")  # Та їх переклад
            if english != ukr:
                f = open('english.txt', 'a')  # Відкриваємо файл
                f.write("\t")  # Робимо відступ
                f.write(english)  # Вставляємо наше слово
                f.close()  # Закриваємо файл
                print("\nВиводим данні з файлу\n")
                print(self.printenglish())
                f2 = open('ukr.txt', 'a')  # Аналоігчні дії для перекладу
                f2.write('\t')
                f2.write(ukr)
                f2.close()
                print(self.printukr())

            else:
                print("Спробуйте ще раз")
                self.add()
        else:
            print("Очищення файлів")
            self.delateall()
            Hello()
    def printenglish(self): # Функція виводу інгліш слів
        file = open('english.txt', 'r') # Відкриваєм файл з аргументом 'a'
        for line in file:
            d = line.split() # Кожен рядок розбиваємо на окремі слова і виходить список
            self.englishlist = d # Записуєм отриманий список в наш стрінг
        file.close() # Закриваємо файл
        return self.englishlist # Повертаємо список

    def printukr(self): # Аналогічно попередньому
        file = open('ukr.txt', 'r')
        for line in file:
            d = line.split()
            self.ukrlist = d
        file.close()
        return self.ukrlist

    def delateall(self):
        f1 = open('english.txt', 'w')  # При аргементі 'w' всі данні файлу перезаписуються
        f2 = open('ukr.txt', 'w')
        f1.close()  # Закриваємо файли
        f2.close()


hello = Hello()
