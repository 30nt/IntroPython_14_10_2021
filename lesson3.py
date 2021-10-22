# Условный оператор if
# тернарный оператор
# форматирование строк, "" ''
# цикл while

############################################

# if условие:
#     блок действий если условие Да
# elif условие2:
#     блок действий если условие2 Да
# elif условие3:
#     блок действий если условие3 Да
# .....
# else:
#     блок действий если Нет

var_1 = -4
value = 1
if var_1 != 4:
    print("True case")
    value = var_1 * 2
else:
    print("false case")
    value = -var_1
print(value)


from random import randint

rand_value = randint(1, 6)

if rand_value > 5:
    new_value = rand_value * 2
else:
    new_value = rand_value * 3

print(rand_value, new_value)

if rand_value < 3:
    print("Победил игрок №1")
elif rand_value < 5:
    print("Победил игрок №2")
elif rand_value < 7:
    print("Победил игрок №3")
else:
    print("Если ты это читаешь, то ты что-то не учел")

if rand_value % 2 == 0:
    print(rand_value, "Четное")
else:
    print(rand_value, "Нечетное")

#################################### приведение к типу bool

value = "False"
bool_value = bool(value)
print(bool_value)
#
# int -> bool | False только для 0
# float -> bool | False только для 0.0
# str -> bool | False только для ""

rand_value = randint(0, 10)
if rand_value:
    print(rand_value, "Не ноль")
else:
    print(rand_value, "Ноль")

if not rand_value % 2:
    print(rand_value, "Четное")
else:
    print(rand_value, "Нечетное")

if 0:
    print("!!!!")

###############################################################################
# тернарный оператор
rand_value = randint(1, 6)
rand_value = 10
if rand_value > 5:
    new_value = rand_value * 2
else:
    new_value = rand_value * 3

new_value = rand_value * 2 if rand_value > 5 else rand_value * 3
# нов_знач = знач_если_да if условие else знач_если_нет
print(rand_value, new_value)

###############################################################################
# форматирование строк, "" ''

new_str = 'New string!'
double_str = "Double"
my_str = "I'm student"
company = '"Apple", LTD'
full_str = '''I'm student in "Apple", LTD'''

value = 5
result = 10
# print('For ', value, 'result is ', result)
print(f"For {value}, result is {result}")

filename = "lesson3.txt"
folder = "HW"
# path = folder + "/" + filename
path = f"{folder}/{filename}"

print(path)

my_str = my_str + "--->"
print(my_str)

my_str = "qwertykasjdfsdgfshvdknxzvahuvism, s"
index = 3
print(my_str[index]) # обращение по индексу
len_my_str = len(my_str)
print(len_my_str, my_str[len_my_str - index], my_str[-index])

new_str = my_str[1:-1]  # срез от .. до. (Правый конец не включаем)
new_str = my_str[-5:-1]
new_str = my_str[:]  # копирование строки
new_str = my_str[::2]  # символы на четных индексах
new_str = my_str[1::2]  # символы на нечетных индексах
new_str = my_str[10:20:5]
new_str = my_str[::-1]  # разворот строки, третий параметр - шаг
print(new_str)

##########################################################################
# цикл while

# while условие:
#     блок, если ДА

value = 10
while value >= 0:
    print(f'Value: {value}')
    value -= 1  # value = value - 1

while True:
    print(f'Value: {value}')
    value -= 1
    if value < 0:
        break

condition = True
while condition:
    print(f'Value: {value}')
    value -= 1
    if value < 0:
        condition = False