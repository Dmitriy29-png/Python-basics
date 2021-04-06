my_str = input('Введите строку : ')
my_str = my_str.split()
for num, elem in enumerate(my_str, 1):
    if len(elem) > 10:
        elem = elem[0:10]
    print(num, elem)
