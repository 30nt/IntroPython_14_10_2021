# Практическая работа. Строки, списки, циклы.



"""
1) У вас есть переменная my_str, тип - str. И переменная my_symbol, тип - str.
Напечатать ЧИСЛО сколько раз my_symbol встречается в my_str.
Пример:  my_str="blablacar", my_symbol="bla".
Вывод на экран:
2
"""
# my_str = "blablacarblablacar"
# my_symbol = "bla"

# res_1 = my_str.count(my_symbol)
# print(res_1)

"""
2) У вас есть переменная my_str, тип - str. И переменная my_symbol, тип - str. 
Напечатать столько раз my_symbol, сколько он встречается в my_str. 
Пример:  my_str="blablacar", my_symbol="bla". 
Вывод на экран:
bla
bla
"""

# for _ in range(res_1):
#     print(my_symbol)

"""
3) У вас есть переменная my_str, тип - str. Напечатать ЧИСЛО сколько 
РАЗНЫХ символов встречается в my_str. 
Большая и маленькая буква считается как одинаковый символ. 
Пробелы, запятые и т.д. считаем тоже как символы.
Пример:  my_str="bla BLA car". 
Вывод на экран:
6
"""
my_str = "bla BLA car"
# my_str_lower = my_str.lower()
# box = []
# for symbol in my_str_lower:
#     if symbol not in box:
#         box.append(symbol)
# res_3 = len(box)
# print(res_3)


"""
4)
Дана строка my_str и пустой список my_list.
Заполнить my_list символами из my_str, 
которые стоят на четных местах в строке (считаем с 0)
"""
my_str = "qwerty1"
my_list = []
# print(id(my_list))
#
# for index, symbol in enumerate(my_str):
#     if not index % 2:  # если index = 2, то index % 2 это 0. Тогда 0 это False. False- значит брать нельзя. Поэтому not index % 2 это True.Значит берем.
#         my_list.append(symbol)
#
# # my_list += list(my_str[::2])  # НЕ ТО ЖЕ ЧТО my_list = my_list + list(my_str[::2])
# print(id(my_list), my_list)

"""
5)
Дана строка my_str, список str_index целых чисел в диапазоне от 
0 до длинны строки минус 1, пустой список my_list.
Заполнить my_list символами из my_str, которые стоят на местах с 
индексами из str_index
"""
my_str = "qwerty"
my_list = []
str_index = [3, 2, 5, 5, 1, 0, 5, 0, 3, 2, 1]

# for index in str_index:
#     my_list.append(my_str[index])
# print(my_list)

"""
8)
Дано целое число (int). Определить сколько цифр в этом числе.
"""
my_number = 7812481234125126354123641275238541034182680000000000000

# res_8 = len(str(my_number))
# print(res_8)

"""
9)
Дано целое число. Определить наибольшую цифру в этом числе.
"""

# my_number_str = str(my_number)
# my_number_str = "qwertDHGBKJL"
# max_symbol = min(my_number_str)  # для строк используется таблица ASCII символов
# print(max_symbol)
# print(ord("@"), chr(100))

"""
10)
Дано целое число. Составить число (int) с цифрами в обратном порядке.
"""
# my_number_str = str(my_number)
# new_number = int(my_number_str[::-1])
# print(new_number)

"""
11)
Дано целое число. Составить число с цифрами в порядке возрастания(убывания).
"""
# .sort() - сортирует текущий объект (изменяемый)
# sorted() - создает новый отсортированный объект

# my_number_str = str(my_number)
# my_number_sort = sorted(my_number_str, reverse=True)
# new_number_str = "".join(my_number_sort)
# new_number = int(new_number_str)
# print(new_number)

# new_number = int("".join(sorted(str(my_number))))
# print(new_number)