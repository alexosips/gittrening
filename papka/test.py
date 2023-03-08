import math
global y
x = float(input("Введіть значеннь x ="))
if x < -2:
    y = 1
elif x >= -2 and x < 0:
     y = -(1/2) * x - 0
elif x >= 0 and x > 2:
    y =math.sqrt(4+x ** 2)
elif x <= 2 and x >= 0:
    y = math.sqrt(x-4 ** 2)
elif x >= 4 and y==0:
    y = (2/3)*6
print("X = {0: .2f}  Y ={1: .2f}".format(x, y))
