import requests
import xml.etree.ElementTree as et
from decimal import Decimal
from datetime import datetime

def currency_rates(currcode):
    currcode = currcode.lower()
    request = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    date = None
    if "Date" in request.headers:
        date = datetime.strptime(request.headers["Date"], "%a, %d %b %Y %H:%M:%S %Z")
    xml = et.fromstring(request.text)
    for valute in xml.findall("Valute"):
        code = valute.find("CharCode")
        if (None != code) and  (currcode == code.text.lower()):
            value = valute.find("Value")
            if (None != value):
                return Decimal(value.text.replace(",", ".")), date
    return None, None
