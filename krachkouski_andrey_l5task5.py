src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = []
for i in range(len(src)):
    uniq = True
    for j in range(len(src)):
        if (i != j) and (src[i] == src[j]):
            uniq = False
            break
    if uniq:
        result.append(src[i])
print(src)
print(result)

result = [i for i in src if (1 == src.count(i))]
print(result)

# result = [23, 1, 3, 10, 4, 11]
