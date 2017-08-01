# Два поезда движутся на скорости V1 и V2 навстречу друг другу.
# Между ними 10 км. пути. Через 4 км пути первый поезд может свернуть на запасной путь.
# При заданных скоростях узнать столкнутся ли поезда.

v1 = int(input(print("Enter first speed")))
v2 = int(input(print("Enter second speed of train")))


def is_crush():
    t1 = 4 / v1
    s1 = t1 * v2

    if s1 >= 6:
        return True
    else:
        return False


print(is_crush())
