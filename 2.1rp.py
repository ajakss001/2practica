class Student:
    def __init__(self, surname, birth_date, group_number, grades):
        self.surname = surname
        self.birth_date = birth_date
        self.group_number = group_number
        self.grades = grades

    def update(self, surname=None, birth_date=None, group_number=None):
        if surname:
            self.surname = surname
        if birth_date:
            self.birth_date = birth_date
        if group_number:
            self.group_number = group_number

    def get_average_grade(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0

    def __str__(self):
        return (f"Фамилия: {self.surname}\n"
                f"Дата рождения: {self.birth_date}\n"
                f"Номер группы: {self.group_number}\n"
                f"Успеваемость: {self.grades}\n"
                f"Средний балл: {self.get_average_grade():.2f}")

def find_student(students, surname, birth_date):
    for student in students:
        if student.surname == surname and student.birth_date == birth_date:
            return student
    return None

def main():
    students = [
        Student("Иванов", "2000-01-15", "Группа 1", [4, 5, 3, 4, 5]),
        Student("Бехоев", "1998-05-20", "Группа 2", [3, 3, 4, 2, 5]),
        Student("Машнец", "2007-03-10", "Группа 1", [5, 4, 4, 5, 5])
    ]

    students[0].update(surname="Иванова", birth_date="2000-01-16", group_number="Группа 2")

    print("Информация о студентах:")
    for student in students:
        print(student)
        print("-" * 30)

    search_surname = input("Введите фамилию студента для поиска: ")
    search_birth_date = input("Введите дату рождения студента (YYYY-MM-DD): ")

    found_student = find_student(students, search_surname, search_birth_date)

    if found_student:
        print("Студент найден:")
        print(found_student)
    else:
        print("Студент не найден.")

if __name__ == "__main__":
    main()