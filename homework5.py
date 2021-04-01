proceeds = float(input('Введите выручку фирмы: '))
cost = float(input('Введите издержки фирмы: '))
if proceeds > cost:
    print(f'Фирма работает с прибылью. Рентабильность выручки составило: {proceeds / cost:.2f}')
    working = int(input('Введите количество работников: '))
    print(f'Прибыль фирмы с расчетом на одного сотрудника: {proceeds / working:.2f}')
elif proceeds == cost:
    print('Ваша фирма выходит в ноль!')
else:
    print('Ваша фирма в убытке!!!')

