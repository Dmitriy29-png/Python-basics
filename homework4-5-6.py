# -*- coding: utf-8 -*-
class Sklad:
    def __init__(self):
        self._dict = {}

    def add_to(self, equipment):

        self._dict.setdefault(equipment.name, []).append(equipment)

class Equipment:
    def __init__(self, name, make, price, quantity, year):
        self.name = name
        self.make = make
        self.price = price
        self.quantity = quantity
        self.year = year
        try:
            self.name = input(f'Введите наименование: ')
            self.make = input(f'Введите марку мадели: ')
            self.price = int(input(f'Введите цену за 1шт: '))
            self.quantity = int(input(f'Введите количество штук: '))
            self.year = int(input(f'Введите год  товара : '))
        except:
            return f'Ошибка ввода данных'

        print(f'Для выхода - Q, продолжение - Enter')
        q = input(f'---> ')
        if q == 'Q' or q == 'q':
            return f'Выход'
        else:
            return Equipment()

    def __repr__(self):
        return f'{self.name}-{self.make}-{self.price}-{self.quantity}-{self.year}'


class Printer(Equipment):
    def __init__(self, series, name, make, price, quantity, year):
        super().__init__(name, make, year)
        self.series = series

    def action(self):
        return 'Печатает'


class Scaner(Equipment):
    def __init__(self, name, make, price, quantity, year):
        super().__init__(name, make, price, quantity, year)

    def action(self):
        return 'Сканирует'


class Xerox(Equipment):
    def __init__(self, name, make, price, quantity, year):
        super().__init__(name, make, price, quantity, year)

    def action(self):
        return 'Копирует'


sklad = Sklad()

scaner = Scaner()
sklad.add_to(scaner)
scaner = Scaner()
sklad.add_to(scaner)
scaner = Scaner()
sklad.add_to(scaner)

print(sklad._dict)

print(sklad._dict)
printor = Printer()
sklad.add_to(printor)
print(sklad._dict)

