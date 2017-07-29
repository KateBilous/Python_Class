# Написать функцию, которая будет проверять четность некоторого числа
even_number = int(input("Введите число: "))


def _is_even_number():

    result = even_number % 2
    if result == 0:
        print("Число {} - четное".format(even_number))
        return True
    else:
        print("Число {} - нечетное".format(even_number))
        return False
call_func = _is_even_number()
print(call_func)