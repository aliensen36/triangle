import math
print("Вычисление периметра и площади прямоугольного треугольника")

x = int(input("Введите длину первого катета: x = "))
y = int(input("Введите длину второго катета: y = "))

def square(x, y):
    square = x * y / 2
    return square

def perimeter(x, y):
    h = math.sqrt(x ** 2 + y ** 2) # гипотенуза
    perimeter = x + y + h
    return round(perimeter, 2)

print("Периметр треугольника равен ", perimeter(x, y))
print("Площадь треугольника равна ", square(x, y))
