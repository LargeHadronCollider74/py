import utils
import sys

if (1 < len(sys.argv)):
    res, date = utils.currency_rates(sys.argv[1])
    print(res, date)
    print(type(res), type(date))
else:
    print('Using: "l4 task5.py" currency_code')
