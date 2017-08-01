# Написать функцию, которая отвечает на вопрос,
#  пересекаются ли две заданные окружности на плоскости. Каждая окружность задается координатами центра и радиусом
import math

r1 = int(input(print(" Enter radius of circle 1  r1 = ")))
r2 = int(input(print(" Enter radius of circle 1  r2 = ")))
x1 = int(input(print(" Enter coordinates of circle 1  x1 = ")))
y1 = int(input(print(" Enter coordinates of circle 1  y1 = ")))
x2 = int(input(print(" Enter coordinates of circle 1  x2 = ")))
y2 = int(input(print(" Enter coordinates of circle 1  y2 = ")))


def is_circles_crosses():
    cat1 = abs(x1 - x2)
    cat2 = abs(y1 - y2)
    dist_of_cent = math.sqrt(cat1 ** 2 + cat2 ** 2)
    circle_dist = dist_of_cent - r1 - r2
    big_rad = max(r1, r2)
    small_rad = min(r1, r2)

    if circle_dist > 0:
        return False

    elif dist_of_cent + small_rad < big_rad:
        return False

    else:
        return True


call_func = is_circles_crosses()
print(is_circles_crosses())
