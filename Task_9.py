# Написать программу, которая переводит в верхний регистр второе
#  слово (слово - последовательность символов между двумя пробелами). Например: “abc def ghj” -> “abc DEF ghj”


def lower_cas2uppercase(one_word):
    one_word.split()
    f_st = one_word.split()[0]
    s_nd = one_word.split()[1]
    t_rd = one_word.split()[2]
    uppercase = s_nd.upper()
    return print(f_st, uppercase, t_rd)


call_def = lower_cas2uppercase("alex alex G")
