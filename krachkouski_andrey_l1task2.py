lst = list(range(1,1000,2))
result = 0
for i in range(len(lst)):
    lst[i] = lst[i] ** 3
    num = lst[i]
    sum = 0
    while (0 < num):
        sum = sum + (num % 10)
        num = num // 10
    if (0 == (sum % 7)):
        result = result + lst[i]

print(lst)
print(result)

result = 0
for i in range(len(lst)):
    lst[i] = lst[i] + 17
    num = lst[i]
    sum = 0
    while (0 < num):
        sum = sum + (num % 10)
        num = num // 10
    if (0 == (sum % 7)):
        result = result + lst[i]

print(lst)
print(result)


