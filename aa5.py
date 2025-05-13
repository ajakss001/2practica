class SampleEntity:
    def __init__(self, attribute_one=None, attribute_two=None):
        if attribute_one is not None and attribute_two is not None:
            self.attribute_one = attribute_one
            self.attribute_two = attribute_two
            print(f"Объект создан с данными: {self.attribute_one}, {self.attribute_two}")
        else:
            self.attribute_one = "Значение по умолчанию A"
            self.attribute_two = "Значение по умолчанию B"
            print("Объект создан с стандартными значениями")

    def __del__(self):
        print(f"Объект {self} был уничтожен из памяти")


def demonstrate():
    print("Создаем первый объект с конкретными данными:")
    first_instance = SampleEntity("Данные 1", "Данные 2")

    print("\nСоздаем второй объект со стандартными значениями:")
    second_instance = SampleEntity()

    print("\nОбъекты созданы. Сейчас удалим их вручную.")

    del first_instance
    del second_instance

demonstrate()