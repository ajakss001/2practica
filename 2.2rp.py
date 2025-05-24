class Train:
    def __init__(self, destination, train_number, departure_time):
        self.destination = destination
        self.train_number = train_number
        self.departure_time = departure_time

    def __str__(self):
        return f"Поезд №{self.train_number}, Пункт назначения: {self.destination}, Время отправления: {self.departure_time}"

def main():
    trains = [
        Train("Архангельск", "111", "10:00"),
        Train("Томск", "70", "12:30"),
        Train("Красноярск", "124", "15:45"),
        Train("Новосибирск", "154", "18:20")
    ]

    print("Доступные поезда:")
    for train in trains:
        print(train)

    search_number = input("Введите номер поезда для поиска: ")

    found_trains = [train for train in trains if train.train_number == search_number]
    if found_trains:
        print("Найденные поезда:")
        for train in found_trains:
            print(train)
    else:
        print("Поезд не найден.")

if __name__ == "__main__":
    main()