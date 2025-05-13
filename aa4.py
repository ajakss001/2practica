class StepTracker:
    def __init__(self, start_value=0):
        self._current_count = start_value

    @property
    def current_value(self):
        return self._current_count

    def increment(self):
        self._current_count += 1
        print(f"Увеличили ➔ {self._current_count}")

    def decrement(self):
        self._current_count -= 1
        print(f"Уменьшили ➔ {self._current_count}")

    def reset(self, new_value=0):
        self._current_count = new_value
        print(f"Сброс! Новое значение: {self._current_count}")


def demonstrate_counter():
    print("\n🔢 Демонстрация работы счётчика 🔢")

    default_counter = StepTracker()
    custom_counter = StepTracker(10)

    print(f"\nСчётчик 1 (по умолчанию): {default_counter.current_value}")
    print(f"Счётчик 2 (с начальным значением): {custom_counter.current_value}")

    print("\nИзменяем счётчик 1:")
    default_counter.increment()
    default_counter.increment()
    default_counter.decrement()

    print("\nИзменяем счётчик 2:")
    custom_counter.decrement()
    custom_counter.decrement()
    custom_counter.increment()

    print("\nСбрасываем счётчик 1:")
    default_counter.reset(5)

    print("\nИтоговые значения:")
    print(f"Счётчик 1: {default_counter.current_value}")
    print(f"Счётчик 2: {custom_counter.current_value}")


if __name__ == "__main__":
    print("██████████████████████████████")
    print("█    СИСТЕМА УПРАВЛЕНИЯ      █")
    print("█        СЧЁТЧИКОМ           █")
    print("██████████████████████████████")

    tracker = StepTracker()

    while True:
        print("\nМЕНЮ:")
        print("1. Увеличить (+1)")
        print("2. Уменьшить (-1)")
        print("3. Показать текущее значение")
        print("4. Сбросить счётчик")
        print("5. Демонстрация работы")
        print("6. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            tracker.increment()

        elif choice == "2":
            tracker.decrement()

        elif choice == "3":
            print(f"\nТекущее значение: {tracker.current_value}")

        elif choice == "4":
            try:
                value = int(input("Введите новое начальное значение: "))
                tracker.reset(value)
            except ValueError:
                print("Ошибка! Введите целое число!")

        elif choice == "5":
            demonstrate_counter()

        elif choice == "6":
            print("Работа программы завершена")
            break

        else:
            print("Неверный ввод, попробуйте снова")