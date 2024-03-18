import math

x = float(input("Введите число X: "))
y = float(input("Введите число Y: "))


def f1(x, y):
    p1 = x * 2 + 56 - y / x + math.cos(x * math.pi)
    p2 = int(p1)
    return p1, p2


def f2(x, y):
    p1 = float((math.log(27) ** (x * y)) + 9 * (x - y))
    p2 = int(p1)
    return p1, p2


print("Первое вычисление: ", f1(x, y))
print("Второе вычисление: ", f2(x, y))
