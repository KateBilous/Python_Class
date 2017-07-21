# Написать программу, которая берет две строки и помещает первую строку в середину второй.
# Результат помещается в середину первой. Длину строки можно получить с помощью функции len().
#  Для простоты можно считать, что длины строк четные. Программа должна быть универсальной, т.е. не зависеть от длины строк

str1 = "  I may be able to pull a few strings for you if you need the document urgently"
str2 = "By pulling strings he got us house seats to the opening, " \
       "or His father pulled some wires and got him out of jail."

dev_str1 = len(str1) // 2
dev_str2 = len(str2) // 2
print(dev_str1)

first_st_task = str2[:dev_str2] + str1 + str2[dev_str2:]
print(first_st_task)

second_task = str1[:dev_str1] + str2 + str2[dev_str1:]
print(second_task)



