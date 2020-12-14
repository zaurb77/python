# Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

my_list = ['Ciao',                                      # string
           True,                                        # bool
           2.5,                                         # float
           18,                                          # int
           8 + 15j,                                     # complex
           [5, 'cacao', [2.2, 'Torino', False]],        # list
           {'1:5', 'name:"Tony'},                       # set
           frozenset({'1:5', 'name:"Vera'}),            # frozenset
           {'name': 'Zaur', 'age': '42'},               # dictionary
           tuple('Bahramov')                            # tuple
           ]
print(my_list)
col_width = 42
for i in my_list:
    print(f'{str(i):{col_width}} ==>\t{str(type(i)):{col_width}}')


# то же самое с использованием 'repr'
print('\n')
print('================= То же самое с использованием repr =======================')
my_list = ['Ciao',                                      # string
           True,                                        # bool
           2.5,                                         # float
           18,                                          # int
           8 + 15j,                                     # complex
           [5, 'cacao', [2.2, 'Torino', False]],        # list
           {'1:5', 'name:"Tony'},                       # set
           frozenset({'1:5', 'name:"Vera'}),            # frozenset
           {'name': 'Zaur', 'age': '42'},               # dictionary
           tuple('Bahramov')                            # tuple
           ]
print(my_list)
col_width = 42
for i in my_list:
    print(f'{repr(i):{col_width}} ==>\t{str(type(i)):{col_width}}')