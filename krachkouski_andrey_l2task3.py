import re

lst = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

#print(id(lst))
i = 0
while i < len(lst):
    sign = ""
    if ((0 < len(lst[i])) and (lst[i][0] in ("+","-"))):
        sign = lst[i][0]
        lst[i] =  lst[i][1:]
    if (lst[i].isnumeric()):
        lst[i] = f"{int(lst[i]):02d}"
        lst.insert(i, '"')
        lst.insert(i + 2, '"')
        i = i + 1
    if (0 < len(sign)):
        lst[i] = f"{sign}{lst[i]}"
    i = i + 1

#print(id(lst))
print(lst)
result = " ".join(lst)
print(result)
lts2 = re.split(r'(" [+-]?\d+ ")', result)
for i in range(len(lts2)):
    if (re.match(r'" [+-]?\d+ "', lts2[i])):
        lts2[i] = lts2[i].replace(" ", "")
print("".join(lts2))