class DivToZero(Exception):
    @classmethod
    def raise_if_invalid(x, divider):
        if 0 == divider:
            raise DivToZero
    def __str__(self):
        return "division to zero not allowed"

while True:
    try:
        print("numerator:")
        num = int(input())
        print("divider:")
        div = int(input())
    except KeyboardInterrupt:
        break
    except Exception as e:
        print(e)
    try:
        DivToZero.raise_if_invalid(div)
    except DivToZero as e:
        print(e)
        continue
    print(f"result = {float(num) / float(div)}")
