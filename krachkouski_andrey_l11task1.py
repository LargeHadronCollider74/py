import re
import datetime

class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def Convert(x, date):
        result = re.findall(r"(\d{1,2})-(\d{1,2})-(\d{1,4})", date)
        try:
            day = int(result[0][0])
            month = int(result[0][1])
            year = int(result[0][2])
            if (100 > year):
                year = year + 2000
            return day, month, year
        except:
            return None, None, None

    @staticmethod
    def IsValid(date):
        day, month, year = Date.Convert(date)
        if day and month and year:
            try:
                datetime.date(year, month, day)
                return True
            except:
                pass
        return False


x = Date("12-1-21")
print(Date.Convert("12-1-21"))
print(Date.Convert("12-1-1921"))
print(Date.Convert("12-50-21"))
print(Date.IsValid("12-1-21"))
print(Date.IsValid("12-50-21"))
