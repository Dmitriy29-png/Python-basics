# Не работает
my_list = [6, 9, 3, 1, 5, 5, 8, 9]
print(f'Рейтинг - {my_list}')

num_rating = int(input('Введите число : '))
for el in range(len(my_list)):
    if (my_list[el]) == num_rating:
        my_list.insert(el + 1, num_rating)
        break
    elif my_list[0] < num_rating:
        my_list.insert(0, num_rating)
    elif my_list[-1] > num_rating:
        my_list.append(num_rating)

print(f'Текуший рейтинг - {my_list}')
num_rating = int(input('Введите число : '))

