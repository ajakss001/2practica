class Counter:
    def __init__(self, initial_value=0):
        self.value = initial_value

    def increase(self):
        self.value += 1

    def decrease(self):
        self.value -= 1

    @property
    def current_value(self):
        return self.value

def main():
    counter = Counter(5)
    print(f"Текущее значение: {counter.current_value}")

    counter.increase()
    print(f"После увеличения: {counter.current_value}")

    counter.decrease()
    print(f"После уменьшения: {counter.current_value}")

    default_counter = Counter()
    print(f"Значение по умолчанию: {default_counter.current_value}")

    default_counter.increase()
    print(f"После увеличения по умолчанию: {default_counter.current_value}")

    default_counter.decrease()
    print(f"После уменьшения по умолчанию: {default_counter.current_value}")

if __name__ == "__main__":
    main()