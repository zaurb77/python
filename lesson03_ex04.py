# Программа принимает действительное положительное число x и целое отрицательное
# число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

# ============ Первое решение с использованием ** ============
# def power(*args):
#     return var_a ** var_b
#
# var_a = int(input("Введите положительное целое число: "))
# var_b = int(input("Введите отрицательное целое число: "))
# print(power(var_a, var_b))

# ============ Второе решение с использованием циклов ============
def power(var_a, var_b):
    while var_b >= 0:
        res = var_a * var_b
        var_b -= 1
    return res

var_a = int(input("Введите положительное целое число: "))
var_b = int(input("Введите отрицательное целое число: "))
my_res = (power(var_a, var_b))
print(my_res)
