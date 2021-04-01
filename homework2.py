num = int(input('Введите число секунд: '))
hour = num // 3600
num = num % 3600
minu = num // 60
seconds = num % 60
print(f"Время: {hour}:{minu}:{seconds}")