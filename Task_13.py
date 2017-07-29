# Пользователь вводит длины катетов прямоугольного треугольника.
#  Написать функцию, которая вычислит и выведет на экран площадь треугольника и его периметр.

# Площадь прямоугольного треугольника S = 1/2 a*b

import math


class SquareAndPerimOfTriangle:
    @staticmethod
    def print_input():
        a = int(input(print("Enter first side")))
        b = int(input(print("Enter second side")))

        return a, b


def print_output():
    print('Площадь треугольника равна', square_of_triangle())
    print('Периметр треугольника равн', perim_of_triangle())


side1, side2 = SquareAndPerimOfTriangle.print_input()


def square_of_triangle():
    square = 0.5 * (side1 * side2)

    return square


def perim_of_triangle():
    c = math.sqrt(side1 ** 2 + side2 ** 2)
    perim = side1 + side2 + c
    return perim


print_output()
