# Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения, город проживания,
# email, телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def user_data(fname, lname, dob, city, email, phone):
    return print(fname, lname, dob, city, email, phone)


fname = input("Введите имя: ")
lname = input("Введите фамилию: ")
dob = input("Введите дату рождения (дд-мм-гггг): ")
city = input("Введите город гдее вы живете: ")
email = input("Введите ваш email: ")
phone = input("Введите ваш номер телефона: ")

user_data(fname, lname, dob, city, email, phone)