# Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который результат спортсмена составит не менее b километров.
# Программа должна принимать значения параметров a и b и  выводить одно натуральное число — номер дня.
# Например: a = 2, b = 3.
# Результат:
# 1-й день: 2
# 2-й день: 2,2
# 3-й день: 2,42
# 4-й день: 2,66
# 5-й день: 2,93
# 6-й день: 3,22
# Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.

first_day = float(input("Сколько км пробежал спортсмен в первый день?: "))
desired_result = float(input("Сколько км должен пробежать спортсмен?: "))

day_num = 1

while desired_result >= first_day:
    print(f"{day_num}-й день: {first_day:.2f}")
    first_day = first_day + first_day * 10 / 100
    day_num += 1

print(f"Результат не менее {desired_result} км достигнут на {day_num}-й день")
