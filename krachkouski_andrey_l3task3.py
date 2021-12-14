def thesaurus(*names):
    result = {}
    for i in range(len(names)):
        key = names[i][0:1]
        if key in result:
            lst = result[key]
        else:
            lst = []
        lst.append(names[i])
        result.update({key: lst})
    return result

dist = thesaurus("Иван", "Петр", "Мария", "Илья")
print(dist)
for k in sorted(dist):
    print(f"{k}: {dist[k]}")
