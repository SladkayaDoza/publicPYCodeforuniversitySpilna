# main.py
# Author: Мухін Владислав, Максим Білошапка, Штельмах Кирил та Конопля Іван
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
    
# Added by: Штельмах Кіріл — функція сортування
def sort_students(db, by="average", reverse=False):
    """
    Сортує список db['students'] на місці.
    by: "average" | "surname" | "course"
    reverse: False (зростання) або True (спадання)
    Повертає відсортований список студентів.
    """
    students = db.setdefault("students", [])

    if by == "average":
        # для студентів без оцінок даємо ключ -1 (нижче будь-якого реального бала 0..100)
        students.sort(key=lambda s: (average_grade(s) if average_grade(s) is not None else -1), reverse=reverse)
    elif by == "surname":
        # сортування за прізвищем, нечутливе до регістру
        students.sort(key=lambda s: (s.get("surname") or "").lower(), reverse=reverse)
    elif by == "course":
        # курс може бути числом або рядком; намагаємось перетворити на int, інакше ставимо великий ключ
        def course_key(s):
            c = s.get("course")
            try:
                return int(c)
            except Exception:
                return float("inf")
        students.sort(key=course_key, reverse=reverse)
    else:
        raise ValueError("Unsupported sort key: use 'average', 'surname' or 'course'")

    return students
    
# Added by: Максим Білошапка — функція видалення студента
def remove_student(db, surname):
    """
    Видаляє студента за прізвищем (перший збіг).
    Повертає True, якщо видалення успішне, інакше False.
    """
    students = db.get("students", [])
    for i, s in enumerate(students):
        if s.get("surname") == surname:
            del students[i]
            return True
    return False

# Added by: Конопля Іван — функція обчислення середнього балу групи
def group_average(db):
    """
    Обчислює середній бал по всіх студентах групи.
    Повертає середнє значення або None, якщо студентів немає.
    """
    students = db.get("students", [])
    if not students:
        return None
    grades = [average_grade(s) for s in students if average_grade(s) is not None]
    return round(sum(grades) / len(grades), 2) if grades else None

# Простий приклад використання
if __name__ == "__main__":
    # додаємо двох студентів як приклад
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

    # початковий стан
    print("=== Before sorting ===")
    print(json.dumps(db, ensure_ascii=False, indent=2))

    # середні бали
    for s in db["students"]:
        print(f"{s['surname']} {s['name']}: avg = {average_grade(s)}")

    # сортуємо за прізвищем (зростання)
    sort_students(db, by="surname")
    print("\n=== After sort by surname ===")
    print(json.dumps(db, ensure_ascii=False, indent=2))

    # сортуємо за середнім балом (спадання)
    sort_students(db, by="average", reverse=True)
    print("\n=== After sort by average (desc) ===")
    print(json.dumps(db, ensure_ascii=False, indent=2))

    # сортуємо за курсом (зростання)
    sort_students(db, by="course")
    print("\n=== After sort by course ===")
    print(json.dumps(db, ensure_ascii=False, indent=2))
    
    # видаляємо студента за прізвищем
    print("\n=== Removing student 'Іваненко' ===")
    if remove_student(db, "Іваненко"):
        print("Студента 'Іваненко' успішно видалено.")
    else:
        print("Студента 'Іваненко' не знайдено.")

    # перевіримо, що він дійсно зник зі списку
    print(json.dumps(db, ensure_ascii=False, indent=2))
