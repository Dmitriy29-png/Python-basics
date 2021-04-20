
class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}
class Position(Worker):
    def get_full_name(self):

        return self.name + " " + self.surname
    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')

working = Position('Dmitriy', 'Eshtokin', 'fitter', 15000, 3000)

print(working.get_full_name())
print(working.get_total_income())