a = int(input("Введите результаты пробежки первого дня в км: "))
b = int(input("Введите общий желаемый результат в км: "))
days = 0
while a < b:
    result = a
    a = (0.1 * a) + a
    days += 1
    print(f'{days} й день: {result:.2f} км')
print(f"Вы достигнете требуемых показателей на {days} день")