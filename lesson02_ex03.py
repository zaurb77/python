# Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц
# (зима, весна, лето, осень). Напишите решения через list и через dict.

list_months =  ['Декабрь', 'Январь', 'Февраль',
                'Март', 'Апрель', 'Май',
                'Июнь', 'Июль', 'Август',
                'Сентябрь', 'Октябрь', 'Ноябрь']
print(list_months)
print(list_months[5])
user_input = int(input("Введите номер месяца: "))
month = int(user_input-1)
print(list_months[month])

if month >= 0 and month <= 3:
    print("Зима")
elif month >= 4 and month <= 5:
        print("Весна")
elif month >= 6 and month <= 9:
        print("Лето")
elif month >= 10 and month <= 12:
        print("Осень")
else:
    print("Ошибка ввода")

