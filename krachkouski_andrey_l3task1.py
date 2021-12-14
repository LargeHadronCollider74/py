def num_translate(num):
    dict = {"zero" : "нуль", "one" : "один", "two" : "два", "three" : "три", "four" : "четыре", "five" : "пять", "six" : "шесть", "sevem" : "семь",
            "eight" : "восемь", "nine" : "девять", "ten" : "десять"}
    num = num.lower()
    result = None
    if (None != result) and (num in dict):
        result = dict[num]
    return result

print(num_translate("oNe"))
print(num_translate("oNeee"))
