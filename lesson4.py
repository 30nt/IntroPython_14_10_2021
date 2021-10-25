# цикл for
# кортежи и списки

############################################################################
my_tuple = (1, 2, 22, "qwe", True, 3.14, None)  # неизменяемый тип данных
print(my_tuple, type(my_tuple))

my_list = [1, 2, 22, "qwe", True, 3.14, None]  # изменяемый тип данных
print(my_list, type(my_list))

new_list = [my_list, my_tuple]
print(new_list)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(matrix[1][2])
print(my_tuple[200:300])

print(list(my_tuple))
print(tuple(my_list))

my_str = "qwerty"
str_list = list(my_str)
print(str_list)
str_tuple = tuple(my_str)
print(str_tuple)

some_list = ["qwe", "asd", "zxc"]
new_str = "/".join(some_list)
print(new_str)

my_tuple = (1, 2, 22, "qwe", True, 3.14, None, [1000])  # неизменяемый тип данных
my_list = [1, 2, 22, "qwe", True, 3.14, None, [1000]]  # изменяемый тип данных

my_list[0] = 100
print(my_list)
# my_tuple[0] = "qwe"  #  ошибка
print(my_tuple)

my_list[-1][0] = "TEST"
print(my_list)

my_tuple[-1][0] = "TUPLE"
print(my_tuple)

my_list = [1, 2, 3]
print(id(my_list))

my_list = [1, 2, 3]
print(id(my_list))

my_list = [1, 2, 3] * 3
print(my_list)

value = 4
my_list = [value] * 4
print(my_list)

value = [4]
my_list = [value.copy(), 1] * 4
print(my_list)
value[0] = 1
print(value)
print(my_list)

my_list = []
print(id(my_list))

my_str = "qwerty"
# my_list = list(my_str)
my_list.append(my_str)
my_list.append("TEST")
for symbol in my_str:
    my_list.append(symbol)
print(id(my_list), my_list)

del_element = my_list.pop() # удаление последнего элемента
print(del_element)

first_element = my_list.pop(0)
print(first_element)

print("".join(my_list[:2] + my_list[5:]))


##########################################################
my_str = "siuhfgislhdisdfukjsgbvjsgdyfu"

for symbol in my_str:
    if symbol not in "eyuioa":
        new_str = symbol * 3
        print(new_str)


index_for_print = 0
add_index = 1

for index in range(len(my_str)):
    if index == index_for_print:
        print(index, my_str[index])
        add_index += 1
        index_for_print += add_index

for item in enumerate(my_str):
    # print(item, type(item))
    index, symbol = item
    if index == index_for_print:
        print(index, symbol)
        add_index += 1
        index_for_print += add_index
