class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        print(f"draw base {self.title}")

class Pen(Stationery):
    def __init__(self):
        # super(Pen, self).__init__("Pen")
        Stationery.__init__(self, "Pen")
    def draw(self):
        # super(Pen, self).draw()
        Stationery.draw(self)
        print("draw pen")

class Pencil(Stationery):
    def __init__(self):
        super(Pencil, self).__init__("Pencil")
    def draw(self):
        Stationery.draw(self)
        print("draw pen")

class Handle(Stationery):
    def __init__(self):
        super(Handle, self).__init__("Handle")
    def draw(self):
        super(Handle, self).draw()
        print("draw pen")

x = Pen()
x.draw()
x = Pencil()
x.draw()
x = Handle()
x.draw()
