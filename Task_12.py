# Написать функцию, которая рассчитывает сумму всех цифр некоторого трехзначного числа,
#  введенного пользователем в консоли, без использования операторов цикла. А теперь и без строк :)

a = int(input("Введите трехзначное число : "))


def sum_of_numbers(a):
    d1 = a % 10
    a = a // 10
    d2 = a % 10
    a = a // 10
    d3 = a % 10
    sum_ = d1 + d2 + d3

    return sum_


print("Сумма чисел равна ", sum_of_numbers(a))
