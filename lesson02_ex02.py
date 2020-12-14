# Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с
# индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

# For a list, implement the exchange of values
# of neighboring elements, i.e. Items with indexes 0 and 1, 2 and 3, etc. are exchanged.
# If the number of elements is odd, save the last one in its place.
# To fill the list of elements, use the input () function.

step = 1

user_list = (input("Input your list separated by space:\n").split())
# print(user_list)
# print(user_list[2])
# user_list.sort()
# 1 2 3 4 5 6 7
# 2 1 4 3 6 5
for index in range(0, len(user_list), 2): # iterate over list, step 2
    if index != len(user_list) - 1: # swap only if we are not at last index
        user_list[index], user_list[index+1] = user_list[index+1], user_list[index]

print(user_list)




