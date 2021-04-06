element = int(input('Введите длину списка: '))
my_list = []
i = 0
el = 0
while i < element:
    my_list.append(input('Введите зачение элемента в списке: '))
    i += 1
print(my_list)
for elem in range(int(len(my_list)/2)):
    my_list[el], my_list[el + 1] = my_list[el + 1], my_list[el]
    el += 2
print(my_list)