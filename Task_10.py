import datetime
import time

# Дана строка вида "Leo Tolstoy*1828-08-28*1910-11-20".
#  В этой строке указаны имя писателя и через символ * даты рождения и смерти.
#  Даты указаны в формате "YYYY-MM-DD". Требуется написать программу,
# которая по переданной строке определит возраст писателя и вернет его имя и возраст.
#  Например, для строки "Leo Tolstoy*1828-08-28*1910-11-20" программа должна вернуть:
#  "Leo Tolstoy", 82. Месяцы и дни можно игнорировать.

str_ = "Leo Tolstoy*1828-08-28*1910-11-20"


def age_determination_by_L_Tolstoy(str_):
    pars_arg = str_.split("*")
    time_of_birth = pars_arg[1]
    time_of_death = pars_arg[2]
    pars_ast1 = int(time_of_birth.split("-")[0])
    pars_ast2 = int(time_of_death.split("-")[0])
    age_author = pars_ast2 - pars_ast1
    return print(age_author)

call_func = age_determination_by_L_Tolstoy(str_)
