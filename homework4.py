rus = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
new_file = []
with open('data3.txt', 'r') as my_file:
    content = my_file.read().split('\n')
    new_file.append(rus[i[0]] + '  ' + i[1])
    print(new_file)

with open('file.txt', 'w') as file_obj_2:
    file_obj_2.writelines(new_file)