value_int = 12
print(value_int, type(value_int))

value_float = 50.99
print(value_float, type(value_float))

value_str = "-50.3"
print(value_str, type(value_str))

new_value = value_str  # Ctrl + ?
print(new_value)

result = value_str + value_str
result = "QWE" * 12

result = 13 // 2  # целая часть от деления
result = 13 % 5  # остаток от деления
print(result)

###########################################################################
result_int_to_float = float(value_int)
print(result_int_to_float, type(result_int_to_float))

result_str_to_float = float(value_str)  # если это возможно
print(result_str_to_float, type(result_str_to_float))

result_float_to_int = int(value_float)  # НЕ математическое округление
print(result_float_to_int, type(result_float_to_int))

result_str_to_int = int(value_str)  # если это возможно
print(result_str_to_int, type(result_str_to_int))

result_int_to_str = str(value_int)
print(result_int_to_str, type(result_int_to_str))

result_float_to_str = str(value_float)
print(result_float_to_str, type(result_float_to_str))

res = result_int_to_str + result_float_to_str
print(res)

int_ = 12
print(int_)

user_value = input("Введи целое число:")
user_value = int(user_value)
# user_value = int(input("Введи целое число:"))
result = user_value * 10
print(type(user_value), result)

####################################################################
my_bool = False
print(my_bool, type(my_bool))


# my_bool = 2 > 1
my_bool = 2 != 20  # >  <  >=  <=  ==  !=
print(my_bool)

value = 12
my_bool = 3 < value < 100
print(my_bool)

my_bool = "qw" in "qwerty"
print(my_bool)

my_bool = "q" not in "qwerty"
print(my_bool)

negative_my_bool = not my_bool
print(negative_my_bool)

# and (логическое И)
#   T F чай
# T T F
# F F F
# кофе

# or (логическое ИЛИ)
#   T F чай
# T T T
# F T F
# кофе

value = 120
case_1 = value % 2 == 0
case_2 = value > 100

res_case = case_1 and not case_2
print(res_case)
