# Написать функцию, которая будет проверять четность некоторого числа

def even_number():
    even_number = int(input("Введите число: "))
    result = even_number % 2
    if result == 0:
        print("Число {} - четное".format(even_number))
    else:
        print("Число {} - нечетное".format(even_number))
call_func = even_number()