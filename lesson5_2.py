# Генераторы списков
# множества

# numb_list = []
# for number in range(1, 11):
#     numb_list.append(number ** 2)

# numb_list = [number ** 2 for number in range(1, 11)]
# print(numb_list)

# alphabet_index = [index for index in range(ord('a'), ord('z') + 1)]
# print(alphabet_index)
#
# alphabet = [chr(index) for index in range(ord('a'), ord('z') + 1)]
# alphabet = "".join(alphabet)
# print(alphabet)

# numbers = [4, 25, -12, -81, -36]
#
# results = [number ** 0.5 for number in numbers if number > 0]
# print(results)


################################### множества set

my_str = "qqqqqqqqqqqqqqqqqqwertyyyyyyyyyyyyyyyyyyyyyyyy"
# my_list = [1, -3, 2, 5]
#
# str_set = set(my_str)  # изменяемый тип данных, порядок не сохраняется
# print(str_set)
#
# list_set = set(my_list)
# print(list_set)
#
# my_str = "bla BLA car"
# res = len(set(my_str.lower()))
# print(res)
single_symbols = []
for symbol in set(my_str):
    print(symbol, my_str.count(symbol))
    if my_str.count(symbol) == 1:
        single_symbols.append(symbol)
print(single_symbols)

# str_set = set(my_str)
# print(str_set, type(str_set))

ip_list_1 = ["127.0.0.1", "23.45.1.1", "127.0.0.1", "127.0.0.1"]
ip_list_2 = ["127.0.0.3", "23.45.1.1", "127.0.0.10", "127.0.0.10"]
# ip_list = list(set(ip_list_1))  # очистка списка от дублей. Порядок не сохранится.
# print(ip_list)

result_intersection = set(ip_list_1).intersection(set(ip_list_2))

result_union = set(ip_list_1).union(set(ip_list_2))

result_difference = set(ip_list_2).difference(set(ip_list_1))

# print(result_difference)