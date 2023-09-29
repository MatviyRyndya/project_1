marks = []
mark = int(input("Введи оцінку (0 - зупинити введення):"))
three = 0
four = 0
five = 0
while mark != 0:
    marks.append(mark)
    if mark == 3:
        three += 1
    if mark == 4:
        four += 1
    if mark == 5:
        five += 1
    mark = int(input("Введи оцінку (0 - зупинити введення):"))

ss = (three + four + five)/len(marks)*100
print('Список оцінок:', marks)
print('Успішність:',ss)
