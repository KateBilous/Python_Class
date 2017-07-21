# Преобразовать строку с американским форматом даты в европейский. Например, "05.17.2016" преобразуется в "17.05.2016"

american_format = "05.17.2016"
pars_int_arg = american_format.split(".")

month = pars_int_arg[0]
day = pars_int_arg[1]
year = pars_int_arg[2]

print("european format date ", day + "." + month + '.' + year)






