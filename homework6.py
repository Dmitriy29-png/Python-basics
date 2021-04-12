from itertools import count

for el in count(int(input('Введите стартовое число '))):
    if el > 10:
        break
    else:
        print(el)

from itertools import cycle

c = 0
my_list = [True, 'ABC', 123, None]
for el in cycle(my_list):
    if c > 10:
        break
    print(el)
    c += 1

    print(el)