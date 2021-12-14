import requests
import xml.etree.ElementTree as et
from decimal import Decimal

def currency_rates(currcode):
    currcode = currcode.lower()
    request = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    xml = et.fromstring(request.text)
    for valute in xml.findall("Valute"):
        code = valute.find("CharCode")
        if (None != code) and  (currcode == code.text.lower()):
            value = valute.find("Value")
            if (None != value):
                return Decimal(value.text.replace(",", "."))
                # return float(value.text.replace(",", "."))
    return None

# def currency_rates(currcode):
#     currcode = currcode.lower()
#     request = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
#     for i in request.text.split("<CharCode>"):
#         if (0 < len(i)) and ("<" != i[0]):
#             start = i.find("</")
#             if (-1 != start):
#                 code = i[0:start].lower()
#                 if (code == currcode):
#                     start = i.find("<Value>")
#                     if (-1 < start):
#                         start = start + len("<Value>")
#                         end = i.find("</Value>", start)
#                         if (-1 < end):
#                             return float(i[start:end].replace(",", "."))
#     return None

res = currency_rates("Huf")
print(res)
print(type(res))
