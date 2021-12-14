class IsNotNumeric(Exception):
    @classmethod
    def Validate(x, val):
        num = val.split(".")
        if 2 < len(num):
            raise IsNotNumeric
        for x in num:
            if not x.isnumeric():
                raise IsNotNumeric
        return float(val)
    def __str__(self):
        return "is not numeric"

lst = []
print("type stop for exit")
while True:
    try:
        print(f"current list len {len(lst)}")
        print("next ?")
        val = input()
        if "stop" == val.strip().lower():
            break
        lst.append(IsNotNumeric.Validate(val))
    except KeyboardInterrupt:
        break
    except Exception as e:
        print(e)
print(lst)