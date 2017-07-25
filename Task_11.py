# Написать функцию, которая будет переводить градусы в радианы.
#  Используя эту функцию вывести на экран значения косинусов углов в 60, 45 и 40 градусов

import math


# math.cos(X) - косинус X (X указывается в радианах).
#
# math.radians(X) - конвертирует градусы в радианы.

def convert_deg2rad(deg1, deg2, deg3):
    arg_deg1 = math.cos(deg1)
    arg_deg2 = math.cos(deg2)
    arg_deg3 = math.cos(deg3)
    convert_rad1 = math.radians(arg_deg1)
    convwert_rad2 = math.radians(arg_deg2)
    convwert_rad3 = math.radians(arg_deg3)
    return convert_rad1, convwert_rad2, convwert_rad3


check_func = convert_deg2rad(60, 45, 40)
print(check_func)
