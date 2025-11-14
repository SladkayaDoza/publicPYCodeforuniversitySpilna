# Усі студенти працюють з одним і тим самим файлом
FILE_NAME = "group_qna.txt"


def create_file_first_student():
    """
    Створити текстовий файл і записати перший блок даних.

    Структура одного блоку у файлі:
    STUDENT: <прізвище>
    ANSWER:
    <одна або декілька стрічок відповіді>
    QUESTION:
    <одна або декілька стрічок питання>

    Між блоками – порожній рядок.
    """
    try:
        with open(FILE_NAME, "w", encoding="utf-8") as f:
            f.write("STUDENT: Мухін Владислав Аркадійович\n")
            f.write("ANSWER:\n")
            f.write("відповідь буде додана другим студентом.\n")
            f.write("QUESTION:\n")
            f.write("Як у Python відкрити текстовий файл та зчитати всі рядки у список?\n")
            f.write("\n")

        print("Файл успішно створено першим студентом.")
    except OSError as e:
        # Обробка будь-яких помилок роботи з файлом
        print("Помилка під час створення або запису файлу:", e)


def append_student_block(surname, answer_lines, question):
    """
    Дописати до файлу блок наступного студента.
    surname      – прізвище студента (рядок)
    answer_lines – список рядків розгорнутої відповіді
    question     – текст питання для наступного студента
    """
    try:
        with open(FILE_NAME, "a", encoding="utf-8") as f:
            f.write("STUDENT: " + surname + "\n")
            f.write("ANSWER:\n")
            for line in answer_lines:
                f.write(line + "\n")
            f.write("QUESTION:\n")
            f.write(question + "\n")
            f.write("\n")

        print("Блок студента успішно дописано у файл.")
    except FileNotFoundError:
        # Якщо файл ще не створив перший студент
        print("Файл не знайдено. Спочатку його повинен створити перший студент.")
    except OSError as e:
        print("Помилка під час дописування у файл:", e)


if __name__ == "__main__":
    # === ВИКОРИСТАННЯ ===
    # 1) Перший студент:
    #    розкоментувати рядок нижче, запустити файл один раз.
    # create_file_first_student()

    # 2) Другий (і наступні) студенти:
    #    розкоментувати блок нижче, змінити прізвище / відповідь / питання
    
    answer = [ 
        "with open(\"file.txt\", \"r\", encoding=\"utf-8\") as f:", # Відповідь може займати кілька рядків, кожен рядок - елемент у списку
        "   lines = f.readlines()"
    ]
    new_question = "Які типи данних існують в Python?"
    append_student_block("Конопля І.І.", answer, new_question)
    