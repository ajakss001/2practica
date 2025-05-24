class Calculation:
    def __init__(self):
        self.calculation_line = ""

    def update(self, new_line):
        self.calculation_line = new_line

    def add(self, symbol):
        self.calculation_line += symbol

    def get(self):
        return self.calculation_line

    def last(self):
        return self.calculation_line[-1] if self.calculation_line else None

    def remove_last(self):
        if self.calculation_line:
            self.calculation_line = self.calculation_line[:-1]

if __name__ == "__main__":
    calc = Calculation()
    calc.update("10 * 2")
    print(calc.get())

    calc.add("+")
    print(calc.get())

    print(calc.last())

    calc.remove_last()
    print(calc.get())