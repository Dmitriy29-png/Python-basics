
with open('test.txt', 'w+') as my_f:
    line = input('Введите текст:\n')
    while line:
        my_f.write(line + '\n')
        line = input('Введите текст:\n')
        if not line:
            break
    my_f.seek(0)
    content = my_f.read()
    print(content)


