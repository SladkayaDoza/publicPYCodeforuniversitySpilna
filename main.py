# main.py
# Author: Мухін Владислав
# Role: створив початкову структуру словника та функцію додавання
# Date: 2025-10-21

import json
from statistics import mean

# Початковий словник
db = {
    "group_number": "KN-43",    # номер групи
    "students": []              # список студентів
}

# Додавання студента у словник
def add_student(db, surname, name, patronymic, course, subjects):
    student = {
        "surname": surname,
        "name": name,
        "patronymic": patronymic,
        "course": course,
        "subjects": subjects
    }
    db.setdefault("students", []).append(student)
    return student

# Допоміжна функція — середній бал (необов'язкова для першого завдання, але корисна)
def average_grade(student):
    grades = list(student.get("subjects", {}).values())
    return round(mean(grades), 2) if grades else None

# Простий приклад використання
if __name__ == "__main__":
    # Додаємо двох студентів як приклад
    add_student(db, "Іваненко", "Петро", "Олексійович", 2, {
        "Mathematics": 85,
        "Physics": 78,
        "Programming": 92
    })
    add_student(db, "Петренко", "Марія", "Іванівна", 1, {
        "Mathematics": 90,
        "English": 88,
        "Programming": 95
    })

    # Вивід у форматі JSON для зручності
    print(json.dumps(db, ensure_ascii=False, indent=2))

    # Приклад: вивести середній бал кожного студента
    for s in db["students"]:
        avg = average_grade(s)
        print(f"{s['surname']} {s['name']}: avg = {avg}")
