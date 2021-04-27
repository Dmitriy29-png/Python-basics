# -*- coding: utf-8 -*-

class DivisionByZero:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def divide_by_zero(divider, denominator):
        try:
            return (divider / denominator)
        except:
            return (f"Деление на ноль недопустимо")


div = DivisionByZero(10, 100)
print(DivisionByZero.divide_by_zero(15, 0))
print(DivisionByZero.divide_by_zero(354, 4))
print(div.divide_by_zero(5678, 0))