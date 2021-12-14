def num_translate_adv(num):
    dict = {"zero" : "нуль", "one" : "один", "two" : "два", "three" : "три", "four" : "четыре", "five" : "пять", "six" : "шесть", "sevem" : "семь",
            "eight" : "восемь", "nine" : "девять", "ten" : "десять"}
    capital = num.istitle()
    num = num.lower()
    result = "none"
    if num in dict:
        result = dict[num]
    if (capital):
        result = result.capitalize();
    return result

print(num_translate_adv("oNe"))
print(num_translate_adv("Two"))
print(num_translate_adv("TwO"))
print(num_translate_adv("oNeee"))
print(num_translate_adv("Neee"))
