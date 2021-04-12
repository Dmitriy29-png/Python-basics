from sys import argv
script_name, time, salary, bonus = argv

try:
    time = int(time)
    salary = int(salary)
    bonus = int(bonus)
    res = (time * salary) + bonus
    print(f'Зарплата сотрудника : {res}')
except ValueError:
    print('This is Not a number')



