import random
"""import math

x = float(input("введіть Х="))

try:
    a = math.log10(0.083)
    b = math.pow(math.e, a)
    n = math.pow(math.e, a/b)
    m = n - 1
    y = math.pow(a+b, n) / (1 + (x / (math.pow(x, m) + math.pow(b, (m - n)))))
    print(y)
except ValueError:
    print("Логарифм від цього числа не можливий")
    
a=input("Введіть значення: ")
a=int(a)
list=[]
for i in range(0, a):
    b=input("Введіть додаток: ")
    b=int(b)
    list.append(b)
print(list)
"""

f = input("Введіть довжину списка: ")
f = int(f)
c = 0
list = []
for i in range(0, f):
    b = input("Введіть додаток: ")
    b = int(b)
    list.append(b)
    c = c + b
    if c >= 40:
        list.remove(b)
        c = c - b
    else:
        pass
print(list)

x = input("Введіть довжину списку: ")
x = int(x)
list = []

for i in range(0, x):
    element = input("Введіть елемент: ")
    element = int(element)
    list.append(element)
    if i == x - 1:
        print(f"Список просто з елементами {list}")
        for g in range(len(list)):
            list[g] = list[g] + random.randint(0, 20)
            if g == x - 1:
                print(f"Список з доданими рандомними значеннями: {list}")
                for h in range(len(list)):
                    list[h] = list[h] / 2
                    if h == x - 1:
                        print(f"Список з діленням: {list}")

    else:
        print("Якась хуйня")




