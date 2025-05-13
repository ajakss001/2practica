class StudentData:
    def __init__(self, surname, birth, group, scores):
        self.surname = surname
        self.birth = birth
        self.group = group
        self.scores = scores

    def editSurname(self, new_surname):
        self.surname = new_surname

    def updateBirth(self, new_birth):
        self.birth = new_birth

    def changeGroup(self, new_group):
        self.group = new_group

    def printInfo(self):
        print(f"\nДанные студента:")
        print(f"Фамилия: {self.surname}")
        print(f"Дата рождения: {self.birth}")
        print(f"Группа: {self.group}")
        print(f"Оценки: {', '.join(map(str, self.scores))}")


def findStudent(students, search_surname, search_birth):
    found = False
    for student in students:
        if student.surname == search_surname and student.birth == search_birth:
            student.printInfo()
            found = True
    if not found:
        print("\nСтудент не найден")


studentBase = [
    StudentData("Морозов", "15.03.2000", "634", [4, 5, 4, 3, 5]),
    StudentData("Агалаков", "22.07.2001", "634", [5, 5, 4, 5, 4]),
    StudentData("Неяскин", "10.11.1999", "632", [3, 4, 3, 4, 4])
]

while True:
    print("\nУправление базой студентов:")
    print("1 - Изменить фамилию")
    print("2 - Изменить дату рождения")
    print("3 - Изменить группу")
    print("4 - Найти студента")
    print("5 - Выйти")

    choice = input("Выберите действие: ")

    if choice == "1":
        old_surname = input("Введите текущую фамилию: ")
        new_surname = input("Введите новую фамилию: ")
        for s in studentBase:
            if s.surname == old_surname:
                s.editSurname(new_surname)
                print("Фамилия изменена")
                break
        else:
            print("Студент не найден")

    elif choice == "2":
        surname = input("Введите фамилию: ")
        new_birth = input("Введите новую дату рождения: ")
        for s in studentBase:
            if s.surname == surname:
                s.updateBirth(new_birth)
                print("Дата рождения обновлена")
                break
        else:
            print("Студент не найден")

    elif choice == "3":
        surname = input("Введите фамилию: ")
        new_group = input("Введите новую группу: ")
        for s in studentBase:
            if s.surname == surname:
                s.changeGroup(new_group)
                print("Группа изменена")
                break
        else:
            print("Студент не найден")

    elif choice == "4":
        surname = input("Введите фамилию для поиска: ")
        birth = input("Введите дату рождения (дд.мм.гггг): ")
        findStudent(studentBase, surname, birth)

    elif choice == "5":
        print("Работа завершена")
        break

    else:
        print("Неверный ввод, попробуйте снова")