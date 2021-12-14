def thesaurus_adv(*names):
    result = {}
    for i in range(len(names)):
        name_surname = names[i].split(" ")
        key_name = name_surname[0][0:1]
        key_surname = name_surname[1][0:1]
        if key_surname in result:
            dict = result[key_surname]
        else:
            dict = {}
        if key_name in dict:
            lst = dict[key_name]
        else:
            lst = []
        lst.append(names[i])
        dict.update({key_name: lst})
        result.update({key_surname: dict})
    return result

dist = thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
print(dist)
