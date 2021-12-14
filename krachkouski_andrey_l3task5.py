import random

def get_jokes(cnt: "repeat count", flag: "uniq words"=False):
    """ лист со словами 1  """
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    """ лист со словами 2  """
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    """ лист со словами 3  """
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    result = []

    """ еслі флаг true, то огранічіваем число шуток максимальной размерностью nouns """
    if (flag):
        cnt = min(cnt, len(nouns))

    """ формируем шутки """
    for i in range(cnt):
        if (flag):
            ind1 = random.randint(0, len(nouns) - 1)
            ind2 = random.randint(0, len(nouns) - 1)
            ind3 = random.randint(0, len(nouns) - 1)
            result.append(f"{nouns[ind1]} {adverbs[ind2]} {adjectives[ind3]}")
            nouns.remove(nouns[ind1])
            adverbs.remove(adverbs[ind2])
            adjectives.remove(adjectives[ind2])
        else:
            result.append(f"{random.choice(nouns)} {random.choice(adverbs)} {random.choice(adjectives)}")

    return result

jokes = get_jokes(flag = True, cnt = 7)
print(jokes)
