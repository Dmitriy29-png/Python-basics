def mu_func(x, y):
    result = x ** y
    print(result)
mu_func(
    x = int(input('Введите число: ')),
    y = int(input('Введите значение степени: '))
)

def mu_func(x, y):
    result = 1
    while y > 0:
        result *= x
        y -= 1
    print(result)

mu_func(
    x = int(input('Введите число: ')),
    y = int(input('Введите значение степени: '))
)