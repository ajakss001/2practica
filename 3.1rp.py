class Worker:
    def __init__(self, name, surname, rate, days):
        self.name = name
        self.surname = surname
        self.rate = rate
        self.days = days

    def get_salary(self):
        return self.rate * self.days

if __name__ == "__main__":
    name = input("Введите имя: ")
    surname = input("Введите фамилию: ")
    rate = float(input("Введите ставку в час: "))
    days = int(input("Введите кол-во отработанных дней: "))

    worker = Worker(name, surname, rate, days)
    print(f"Работяга: {worker.name} {worker.surname}, ЗП: {worker.get_salary()} долларов")