students = []

while True:
    print("\n1. Добавить\n2. Показать всех\n3. Выйти")
    choice = input("Выберите: ")

    if choice == '1':
        first_name = input("Имя: ")
        last_name = input("Фамилия: ")
        patronymic = input("Отчество: ")
        group = input("Группа: ")
        grades_input = input("Оценки (4 числа через пробел): ")
        grades = grades_input.strip().split()
        if len(grades) != 4:
            print("Введите ровно 4 оценки.")
            continue
        try:
            grades = [float(g) for g in grades]
        except:
            print("Оценки должны быть числами.")
            continue
        students.append({
            'имя': first_name,
            'фамилия': last_name,
            'отчество': patronymic,
            'группа': group,
            'оценки': grades
        })
        print("Добавлено.")
    elif choice == '2':
        if not students:
            print("Нет студентов.")
        else:
            for s in students:
                avg = sum(s['оценки'])/4
                print(f"{s['фамилия']} {s['имя']} {s['отчество']}, группа: {s['группа']}, оценки: {s['оценки']}, средний: {avg:.2f}")
    elif choice == '3':
        break
    else:
        print("Некорректный выбор.")