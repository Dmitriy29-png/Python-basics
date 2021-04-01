num = int(input('Введите  целое положительное число: '))
max = num % 10
while num >= 0:
    num = num // 10
    if num % 10 > max:
        max = num % 10
    else:
        print('то максимальное число ', max)
        break