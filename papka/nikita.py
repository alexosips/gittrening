
import math

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
    print("Нікито лох")