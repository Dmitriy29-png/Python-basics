# Не работает
goods = int(input("Введите количество товара "))
n = 1
my_dict = []
my_list = []
my_analys = {}
while n <= goods:
    my_dict = dict({'название': input("введите название "), 'цена': input("Введите цену "),
                    'количество': input('Введите количество '), 'eд': input("Введите единицу измерения ")})
    my_list.append((n, my_dict))
    n += 1
for elem in my_dict.values():
    my_analys = dict({
        'название': my_dict.get('название', elem),
        'цена': my_dict.get('цена', elem),
        'количество': my_dict.get('количество', elem),
        'ед': my_dict.get('ед', elem)
        })
    print(my_analys)
print(my_list)
