# Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и строк и
# сохраните в переменные, выведите на экран.

# представиться пользователю
my_fname = "Zaur"
my_lname = "Bahramov"
my_age = 43
my_city = 'Turin'
# вывести личную информацию
print(f"Hello there! My name is {my_fname} {my_lname}! I'm {my_age} years old and I live in {my_city}\n")

# узнать у пользователя информацию о нём
f_name = input("What is your first name? ")
l_name = input("What is your last name? ")
age = int(input("How old are you? "))
city = input("Which city are you from? ")

print(f"\nNice to meet you, {f_name} {l_name}!")

if my_city != city:
    response = f"Unfortunately we can't take a coffee today, because you live in {city} and I live in {my_city}"
    response_2 = ""
    print(response + "\r\n")
else:
    # предложить выпить кофе
    response = input(f"Great! Would you like to have coffee with me today? (Y/N): ")
    if response == "Y" or response == "y":
        response_2 = "Well, let's meet at 6:30pm then!"
    elif response == "N" or response == "n":
        response_2 = "Well, next time then! Bye!"
    else:
        response_2 = "Sorry, i couldn't understand what you mean..."
# ответ
print(response_2 + "\r\n")
