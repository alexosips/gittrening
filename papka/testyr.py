import math

x = float(input('Введіть значення x: '))

if x >= -6 and x < 3:
    print(-math.sqrt(9 + (x - 6)**2))
elif x >= -6 and x < -3:
    print(3 * x + 3)
elif x >= 0 and x > 3:
    print(math.sqrt(9 + x**2))
    print(-1 * x + 3)
elif x <= 3 and x < 9:
    print(0.5 * x + (-1.5))
else:
    print("Не виконона жодна умова")