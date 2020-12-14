# Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара
# и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
#     (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
#     (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
#     (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
# например название, а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {
#     “название”: [“компьютер”, “принтер”, “сканер”],
#     “цена”: [20000, 6000, 2000],
#     “количество”: [5, 2, 7],
#     “ед”: [“шт.”]
# }

# Создаем меню
menu = {
    1: "Ввести новый товар",
    2: "Просмотреть структуру",
    3: "Вывести аналитику",
    4: "Выйти из программы"
}

# Создаем структуру items
item_no = 0
item_specs = {"Description": "", "price": 0, "quantity": 0, "uom": "pcs"}
item = (0, item_specs)
print(item)

# Создаем структуру goods
goods = []
# print(goods)
# print(len(goods))

# Выводим меню
for key, value in menu.items():
    print(key, '\t', value)

while True:
    user_choice = int(input("> "))
    if 0 < user_choice < 4:
        print('Вы ввели: ', menu[user_choice])

        if (2 <= user_choice <= 3) and len(goods) == 0:
            print("Сначала необходимо ввести хотя бы 1 товар")
        elif user_choice == 2 and len(goods) > 0:
            for i in goods:
                print(i)
        else:
            while True:
                # tmp_list = list(item)
                # tmp_list[0] += 1
                # for key in item_specs:
                #     print(f"Введите {key.upper()}: ")
                #     item_specs[key] = input()
                # item = tuple(tmp_list)
                # item_no += 1
                tmp_list = list(item)
                tmp_list[0] += 1

                for key in item_specs:
                    print(f"Введите {key.upper()}: ")
                    item_specs[key] = input()
                tmp_list[1] = item_specs
                item = tuple(tmp_list)
                print(item)
                goods.insert(item_no, item)
                item_no += 1
                print(goods)
                add_new = input("Добавить еще артикль? (Y/N): ")
                if add_new == 'Y' or add_new == 'y':
                    continue
                else:
                    break
        # print(goods)

    elif user_choice == 4:
        print("Выход из программы...")
        break
    else:
        print("Неверное значение, попробуйте еще раз...")
        continue

# Создаем структуру
# item_no = 1
# item_specs = {"Description": "", "price": 0, "quantity": 0, "uom": "pcs"}


# =============== ЦИКЛ ================#
# while True:
#     user_choice = int(input("> "))
#     if 0 < user_choice < 4:
#         print('Вы ввели: ', menu[user_choice])
#     elif user_choice == 4:
#         print("Выход из программы...")
#         break
#     else:
#         print("Неверное значение, попробуйте еще раз...")
#         continue


# ============= Рабочая версия с Items, без Goods =============== #
# # Создаем меню
# menu = {
#     1: "Ввести новый товар",
#     2: "Просмотреть структуру",
#     3: "Вывести аналитику",
#     4: "Выйти из программы"
# }
#
# # Создаем структуру
#
#
# item_no = 0
# item_specs = {"Description": "", "price": 0, "quantity": 0, "uom": "pcs"}
# item = (0, item_specs)
#
# print(item)
#
# # Выводим меню
# for key, value in menu.items():
#     print(key, '\t', value)
#
# while True:
#     user_choice = int(input("> "))
#     if 0 < user_choice < 4:
#         print('Вы ввели: ', menu[user_choice])
#
#         if 2 <= user_choice <= 3 and item[0] == 0:
#             print("Сначала необходимо ввести хотя бы 1 товар")
#         else:
#             tmp_list = list(item)
#             tmp_list[0] += 1
#             for key in item_specs:
#                 print(f"Введите {key.upper()}: ")
#                 item_specs[key] = input()
#
#             item = tuple(tmp_list)
#             print(item)
#
#     elif user_choice == 4:
#         print("Выход из программы...")
#         break
#     else:
#         print("Неверное значение, попробуйте еще раз...")
#         continue
