my_list = [15, 2, 3, 1, 7, 5, 4, 10]
my_new_list = [el for i, el in enumerate(my_list) if i > 0 and my_list[i] > my_list[i - 1]]
print(f'Исходный список {my_list}')
print(f'Новый список {my_new_list}')


