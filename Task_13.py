# Пользователь вводит длины катетов прямоугольного треугольника.
#  Написать функцию, которая вычислит и выведет на экран площадь треугольника и его периметр.

# Площадь прямоугольного треугольника S = 1/2 a*b
import math
a = int(input("Введите сторону первого катета: "))

b = int(input("Введите сторону второго катета: "))

def square_and_perim_of_triangle():
    square = 0.5 * (a * b)
    c = math.sqrt(a ** 2 + b ** 2)

    perim = a + b + c

    return square, perim


call_func = square_and_perim_of_triangle()
print("Square of triangle and perimeter are: ", square_and_perim_of_triangle())
