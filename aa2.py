class RailTransport:
    def __init__(self, end_point, transport_id, when_go):
        self.end_point = end_point
        self.transport_id = transport_id
        self.when_go = when_go

    def display_data(self):
        print(f"\nСведения о железнодорожном транспорте ID {self.transport_id}:")
        print(f"Конечный пункт: {self.end_point}")
        print(f"Плановое время отправления: {self.when_go}")


def search_transport(all_transports, needed_id):
    is_found = False
    for unit in all_transports:
        if unit.transport_id == needed_id:
            unit.display_data()
            is_found = True
    if not is_found:
        print("\nЖелезнодорожный транспорт с указанным идентификатором отсутствует")


available_transports = [
    RailTransport("Новосибирск", "741К", "06:20"),
    RailTransport("Владивосток", "085СС", "14:55"),
    RailTransport("Екатеринбург", "203М", "09:10"),
    RailTransport("Краснодар", "412Ч", "22:40")
]

while True:
    print("\nМеню системы учета рейсов:")
    print("1 - Поиск по идентификатору")
    print("2 - Отобразить все маршруты")
    print("3 - Завершить работу")

    user_choice = input("Укажите номер операции: ")

    if user_choice == "1":
        search_id = input("Введите идентификатор рейса: ")
        search_transport(available_transports, search_id)

    elif user_choice == "2":
        print("\nЗарегистрированные рейсы:")
        for item in available_transports:
            item.display_data()

    elif user_choice == "3":
        print("Работа программы завершена")
        exit()

    else:
        print("Ошибка ввода, повторите попытку")