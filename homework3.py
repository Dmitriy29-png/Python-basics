season_list = ['Winter', 'Spring', 'Summer', 'Autumn']
season_dict = {'key_1': 'Winter', 'key_2': 'Spring', 'key_3': 'Summer', 'key_4': 'Autumn'}
while True:
    month = input('Введите номер месяца : ')
    if month.isdigit():
        month = int(month)

        if month == 1 or month == 12 or month == 2:
            print(season_dict.get('key_1'))
            print(season_list[0])
            break
        elif month == 3 or month == 4 or month == 5:
            print(season_dict.get('key_2'))
            print(season_list[1])
            break
        elif month == 6 or month == 7 or month == 8:
            print(season_dict.get('key_3'))
            print(season_list[2])
            break
        elif month == 9 or month == 10 or month == 11:
            print(season_dict.get('key_4'))
            print(season_list[3])
            break
        else:
            print('Такого месяца не существует')

    else:
        print('Введен не номер месяца : ')