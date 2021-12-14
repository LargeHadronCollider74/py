class Road:
    __weight = 25
    __wide = 5
    def __init__(self, l, w):
        self.length = l
        self.width = w
    def volme(self):
        return self.length * self.width * Road.__weight * Road.__wide / 1000

x = Road(5000, 20)
print(x.volme())