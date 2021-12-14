class ComplexNumber():
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __add__(self, other):
        return ComplexNumber(self.a + other.a, self.b + other.b)
    def __sub__(self, other):
        return ComplexNumber(self.a - other.a, self.b - other.b)
    def __mul__(self, other):
        return ComplexNumber((self.a * other.a) - (self.b * other.b), (self.a * other.b) + (self.b * other.a))
    def __floordiv__(self, other):
        num = self * ComplexNumber(other.a, -other.b)
        div = other.a**2 + other.b**2
        if 0 == div:
            raise ZeroDivisionError
        return ComplexNumber(num.a // div, num.a // div)
    def __truediv__(self, other):
        num = self * ComplexNumber(other.a, -other.b)
        div = other.a**2 + other.b**2
        if 0 == div:
            raise ZeroDivisionError
        return ComplexNumber(num.a / div, num.a / div)
    def __str__(self):
        sign = "+"
        if 0 > self.b:
            sign = "-"
        return f"{self.a} {sign} {abs(self.b)}i"

z1 = ComplexNumber(1, 3)
z2 = ComplexNumber(4, -5)
print(z1)
print(z2)
print(z1 + z2)
z1 = ComplexNumber(-2, 0)
z2 = ComplexNumber(2, 5)
print(z1)
print(z2)
print(z1 - z2)
z1 = ComplexNumber(1, -1)
z2 = ComplexNumber(3, 6)
print(z1)
print(z2)
print(z1 * z2)
z1 = ComplexNumber(13, 1)
z2 = ComplexNumber(7, -6)
print(z1)
print(z2)
print(z1 / z2)
print(z1 // z2)
