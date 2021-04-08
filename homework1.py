# Первое решение
def div_func(*arg):
    arg_1 = int(input('Введите число : '))
    arg_2 = int(input('Введите разделитель: '))
    if arg_2 != 0:
        res = arg_1 / arg_2
        return res
    else:
        print('Разделитель не может равняться Нулю')
print(f'Ваш результат {div_func()}')
# Второе решение
def div_func2(arg_1, arg_2):
    if arg_2 != 0:
        return arg_1 / arg_2

    else:
        print('Разделитель не может равняться Нулю')
arg_1 = int(input('Введите число : '))
arg_2 = int(input('Введите разделитель: '))
res = div_func2(arg_1, arg_2)
print(res)