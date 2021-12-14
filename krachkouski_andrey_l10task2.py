from abc import ABC, abstractmethod

class Сlothes(ABC):
    def __init__(self, name):
        self.name = name

    @property
    @abstractmethod
    def Total(self):
        pass

class Coat(Сlothes):
    def __init__(self, v):
        super(Coat, self).__init__("Coat")
        self.v = v

    @property
    def Total(self):
        return self.v / 6.5 + 0.5

class Suit(Сlothes):
    def __init__(self, h):
        super(Suit, self).__init__("Suit")
        self.h = h

    @property
    def Total(self):
        return 2*self.h + 0.3


c = Coat(10)
print(c.Total)

s = Suit(10)
print(s.Total)
