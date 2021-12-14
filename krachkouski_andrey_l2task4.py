lst = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

print(lst)

for i in range(len(lst)):
    item = lst[i].strip();
    pos = item.rfind(" ")
    if (-1 < pos):
        print(f'Привет, {item[pos + 1:].capitalize()}!')

