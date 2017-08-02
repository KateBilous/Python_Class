# Написать функцию решения квадратного уравнения
#   a * x ** 2 + b * x + c = 0
# Solution via discriminant

import math


def quadratic_equation(a, b, c):
    D = b ** 2 - 4 * a * c
    if D > 0:
        x1 = (-1 * b + math.sqrt(D)) / (2 * a)
        x2 = (-1 * b - math.sqrt(D)) / (2 * a)
        return x1, x2
    if D == 0:
        x = -1 * b / (2 * a)
        return x, None
    if D < 0:
        return None, None
