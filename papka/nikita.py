#Виведення інфи
print("Нікіта любить мальчиков")
#Записування інфи в змінну
a = input("Введіть значення а: ") #Змінна в даномк випадку називається "a"
print(a) #Виводимо це значення
#Використровуємо f для виведення і змінної і тексту
print(f"Значення а: {a}") # в {} записуємо змінну яку нам потрібно

#Тепер узнаємо скільки буде 2+2

number1 = 2
number2 = 2 #Робимо дві змінні в які випсуємо двойки в типі int (Тип int це цілочисельні значення)
print(f"2+2={number1 + number2}") # Да в {} можна вписувати деякі операції

#Спробуєм все те саме але тепер цифри будуть в типі str(текстовом)
numstr1 = "2"
numstr2 = "2"
print(f"2+2={numstr1 + numstr2}") #Виводимо цю шнягу
#Опа оказується 2+2=22

a = 5
b = 6
c = a + b
print(c)