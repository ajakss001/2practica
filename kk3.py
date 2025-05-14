class Calculator:
    def set_formula(self, text):
        self.formula = text

    def add_symbol(self, char):
        if hasattr(self, 'formula'):
            self.formula += char
        else:
            self.formula = char

    def get_formula(self):
        return getattr(self, 'formula', '')

    def get_last_char(self):
        formula = getattr(self, 'formula', '')
        return formula[-1] if formula else ''

    def delete_last(self):
        if hasattr(self, 'formula') and self.formula:
            self.formula = self.formula[:-1]


calc = Calculator()

calc.set_formula("10+5")
print("Formula:", calc.get_formula())

calc.add_symbol("*2")
print("After adding:", calc.get_formula())

print("Last char:", calc.get_last_char())

calc.delete_last()
print("After delete:", calc.get_formula())