lst = [57.8, 46.51, 97, 2.45, 54.456, 2345.23, 46.453, 8798.6]

print(lst)
print(id(lst))

lst.sort()
print(lst)
print(id(lst))

result = []
for i in range(len(lst)):
    price = str(lst[i]).split(".")
    kop = "00"
    if (1 < len(price)):
        kop = f"{int(price[1])%100:02d}"
    lst[i] = f"{price[0]} ру {kop} коп"

print(lst)
print(id(lst))

print(lst[0:5])
