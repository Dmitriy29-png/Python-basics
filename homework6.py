import re
predm = {}
with open('data6.txt', 'r') as f_6:
    for line in f_6:
        sum_chas = 0
        chac = re.findall(r'\d+', line)
        for i in chac:
            if i.isdigit():
                sum_chas +=int(i)
        predm[line.split()[0]] = sum_chas
    print(predm)
