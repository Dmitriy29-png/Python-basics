from functools import reduce
def mu_func(prev_el, el):
    return prev_el * el
print(f'все элементы : {[el for el in range(100, 1001) if el % 2 == 0]}')
print(reduce(mu_func, [el for el in range(100, 1001) if el % 2 == 0]))