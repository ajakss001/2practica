class SimpleNumberStorage:
    def __init__(self, num1=0, num2=0):
        self.num1 = num1
        self.num2 = num2

    def display(self):
        print(f"Первое число: {self.num1}, Второе число: {self.num2}")

    def change_numbers(self, new_num1, new_num2):
        self.num1, self.num2 = new_num1, new_num2

    def sum(self):
        return self.num1 + self.num2

    def max_value(self):
        return max(self.num1, self.num2)

def main():
    storage = SimpleNumberStorage(3, 7)
    print("Текущее состояние:")
    storage.display()

    storage.change_numbers(10, 5)
    print("После изменения чисел:")
    storage.display()

    print(f"Сумма чисел: {storage.sum()}")
    print(f"Наибольшее значение: {storage.max_value()}")

if __name__ == "__main__":
    main()