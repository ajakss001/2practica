class SimpleNumberBox:
    def __init__(self, num1, num2):
        self.first_number = num1
        self.second_number = num2

    def show_numbers(self):
        print(f"\nЗначения: {self.first_number} и {self.second_number}")

    def change_numbers(self, new_num1, new_num2):
        self.first_number = new_num1
        self.second_number = new_num2
        print("Значения обновлены!")

    def add_numbers(self):
        result = self.first_number + self.second_number
        print(f"Сумма: {result}")
        return result

    def find_larger(self):
        if self.first_number > self.second_number:
            larger = self.first_number
        else:
            larger = self.second_number
        print(f"Большее число: {larger}")
        return larger

if __name__ == "__main__":
    print("="*30)
    print("Программа для работы с числами")
    print("="*30)

    box = SimpleNumberBox(5, 10)

    while True:
        print("\nЧто сделать?")
        print("1 - Посмотреть числа")
        print("2 - Изменить числа")
        print("3 - Посчитать сумму")
        print("4 - Найти большее число")
        print("5 - Выйти")

        выбор = input("Введите номер действия: ")

        if выбор == "1":
            box.show_numbers()
        elif выбор == "2":
            try:
                number1 = int(input("Введите первое число: "))
                number2 = int(input("Введите второе число: "))
                box.change_numbers(number1, number2)
            except:
                print("Ошибка! Введите целые числа.")
        elif выбор == "3":
            box.add_numbers()
        elif выбор == "4":
            box.find_larger()
        elif выбор == "5":
            print("Работа завершена.")
            break
        else:
            print("Неверный ввод. Попробуйте снова.")