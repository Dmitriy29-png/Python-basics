# Первое решение
from itertools import count
from math import factorial
n = int(input("Укажите факториал какого числа ? : "))
def fact(n):
    for el in count(1):
        yield factorial(el)

x = 0
for el in fact(n):
    if x < n:
        print(el)
        x += 1
    else:
        break


# второе решение
def fact(n):
    temp = 1
    for i in range(1, n + 1):
        temp *= i
        yield temp

n = int(input("Укажите факториал какого числа Вы хотели бы узнать? : "))

for el in fact(n):
    print(el)
