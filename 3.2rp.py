class Worker:
    def __init__(self, name, surname, rate, days):
        self.__name = name
        self.__surname = surname
        self.__rate = rate
        self.__days = days

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname

    def get_salary(self):
        return self.__rate * self.__days

if __name__ == "__main__":
    name = input("Введите имя: ")
    surname = input("Введите фамилию: ")
    rate = float(input("Введите ставку в час: "))
    days = int(input("Введите кол-во отработанных дней: "))

    worker = Worker(name, surname, rate, days)
    print(f"Работяга: {worker.get_name()} {worker.get_surname()}, ЗП: {worker.get_salary()} долларов")