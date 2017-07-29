# Написать функцию, которая будет переводить градусы в радианы.
#  Используя эту функцию вывести на экран значения косинусов углов в 60, 45 и 40 градусов

import math


# math.cos(X) - косинус X (X указывается в радианах).
#
# math.radians(X) - конвертирует градусы в радианы.

def convert_deg2rad_and_found_cos(deg):
    convert_celc2rad = math.radians(deg)
    arg_deg1 = math.cos(convert_celc2rad)

    return convert_celc2rad, arg_deg1


check_func = convert_deg2rad_and_found_cos(60)
print(check_func)
