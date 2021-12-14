lst = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

#print(id(lst))
for i in range(len(lst)):
    sign = ""
    if ((0 < len(lst[i])) and (lst[i][0] in ("+","-"))):
        sign = lst[i][0]
        lst[i] =  lst[i][1:]
    if (lst[i].isnumeric()):
        lst[i] = f'"{int(lst[i]):02d}"'
    if (0 < len(sign)):
        lst[i] = f"{sign}{lst[i]}"

#print(id(lst))
print(lst)
print(" ".join(lst))