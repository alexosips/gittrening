import random
""" 1)Вивести будь-яку фразу 50 раз
    2)Вивести список через for (кожен елемент з нового рядка)
    3)Порівняти кожен елмент списка з числом 13(більше менше)
    4)Вивести найбільше значення списка"""

list = []
for i in range(0,50):
    list.append(random.randint(1,100))
print(f"Початковий список\n {list}")

# 1
for i in range(0,50):
    print(f"{i} Putin xuilo")

# 2
for i in range(len(list)):
    print(f"Елемент : {i} -> {list[i]}")

# 3
for i in range(len(list)):
    if list[i] > 13:
        print(f"Element: {list[i]} більше 13")
    elif list[i] < 13:
        print(f"Element: {list[i]} менше 13")
    else:
        print(f"Element: {list[i]} рівно 13")
# 4
print(max(list))
print(min(list))