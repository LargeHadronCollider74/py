class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):
    # def __init__(self, name, surname, position, wage, bonus):
    #     super(Position, self).__init__(name, surname, position, wage, bonus)
    def get_full_name(self):
        return f"{self.name} {self.surname}"
    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]

x = Position("asdasd", "qqweqwe", "asda2qweqwe", 10223, 765765)
print(x.get_full_name())
print(x.get_total_income())