class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        print(f"Name: {self.name}, Surname: {self.surname}")

    def get_total_income(self):
        print(sum(self._income.values()))


example = Position("Igor", "Ivanov", "worker", 500, 100)
example.get_full_name()
example.get_total_income()
