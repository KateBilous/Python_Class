# Найти результат выражения для произвольных значений a,b,c: | a - b | /( a + b)3 - cos( c )

import math

a = 5
b = 7
c = 8

d = abs(a - b)/(a + b) - math.cos(c)

print("Результат выражения для произвольных значений a,b,c: | a - b | /( a + b)3 - cos( c )", d)