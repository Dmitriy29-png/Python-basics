# первое решение
def my_func(**kwargs):
        print(
                f"{kwargs['name']}, "
                f"{kwargs['surname']}, "
                f"{kwargs['year']}, "
                f"{kwargs['city']}, "
                f"{kwargs['email']}, "
                f"{kwargs['telephone']}"
        )

my_func(
        name=input('enter name'),
        surname=input('enter surname'),
        year=int(input('enter year')),
        city=input('enter city'),
        email=input('enter email'),
        telephone=input('input telephone')
        )

# Второе решение

def my_func (name, surname, year, city, email, telephone):
    return ', '.join([name, surname, year, city, email, telephone])
print(my_func(surname = 'Dmitriy', name = 'Eshtokin', year = '1986', city = 'Arhangelsk', email = 'flathome86@mail.ru', telephone = '8-921-473-07-25'))
