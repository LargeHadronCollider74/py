class Cell:
    def __init__(self, count):
        self.count = count
    def __add__(self, other):
        return Cell(self.count + other.count)
    def __sub__(self, other):
        if (self.count < other.count):
            raise ValueError("ValueError")
        return Cell(self.count - other.count)
    def __mul__(self, other):
        return Cell(self.count * other.count)
    def __floordiv__(self, other):
        return Cell(self.count // other.count)
    def __truediv__(self, other):
        return Cell(int(self.count / other.count))
    def make_order(self, row_len = 5):
        result = []
        i = 0
        while i < self.count:
            result.append("".join("*" for _ in range(min(row_len, self.count - i))))
            i = i + row_len
        return "\n".join(result)

x = Cell(6)
print(x.make_order())
x1 = x + Cell(3)
print(x1.make_order())
x2 = x1 - Cell(6)
print(x2.make_order())
x3 = x2 * Cell(6)
print(x3.make_order())
x4 = x3 // Cell(2)
print(x4.make_order())
x5 = x4 / Cell(2)
print(x5.make_order())
