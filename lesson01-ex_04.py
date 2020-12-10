# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

num = int(input("Введите любое целое число: "))

max_num = 0
while num != 0:
    single_num = num % 10
#    print(single_num)  # вывод для проверки
    num //= 10
    if max_num < single_num:
        max_num = single_num

print(f"Самая большая цифра в введенном числе: {max_num}")
