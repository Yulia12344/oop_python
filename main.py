from student import Student
from professor import Professor
from worker import Worker
from student_worker import StudentWorker

def main():
    student = Student(
        "Юлія", "Саліщева", "yulia@example.com", "1234567890", "2006-07-05",
        2023, "Інститут комп'ютерних наук", "Кафедра систем штучного інтелекту"
    )
    professor = Professor(
        "Олена", "Оленова", "olena@example.com", "0987654321", "1985-05-15",
        "Доктор наук", "Філологічний факультет", "Інститут філології", "Кафедра мовознавства"
    )
    worker = Worker(
        "Микола", "Миколайович", "mykola@example.com", "0987654322", "1980-04-10",
        "Інженер", "Завод"
    )
    student_worker = StudentWorker(
        "Данило", "Данилович", "danylo@example.com", "1122334455", "2004-03-10",
        2021, "Асистент", "Університет", "Інститут електроніки", "Кафедра електронних систем"
    )

    print(student.info)
    print(professor.info)
    print(worker.info)
    print(student_worker.info)
    print("\n")

    # Оновлення контактної інформації
    print(student.update_contact_info("email", "ivan_new@example.com"))
    print(student_worker.update_contact_info("phone_number", "1231231234"))
    print("\n")

    # Перегляд оновленої інформації
    print(student.info)
    print(student_worker.info)
    print("\n")

    # Запис на курс з додатковою інформацією
    student.enroll("Математика", {"кредити": 3, "оцінка": "A"})
    student.enroll("Фізика", {"кредити": 4, "оцінка": "B"})
    print(student.enrollments())
    print(student.total_courses())
    print("\n")

    # Видалення курсу
    print(student.drop_course("Математика"))
    print(student.enrollments())
    print("\n")

    # Додавання курсів для професора
    print(professor.add_course("Література"))
    print(professor.add_course("Лінгвістика"))
    print(professor.courses())
    print("\n")

    # Оновлення посади для працівника
    print(worker.update_position("Головний інженер", "Фабрика"))
    print(worker.info)
    print("\n")

    # Оновлення посади для студент-працівника
    student_worker.enroll("Програмування", {"кредити": 5, "оцінка": "A"})
    print(student_worker.update_position("Стажер", "Лабораторія"))
    print(student_worker.work_schedule())
    print(student_worker.total_courses())
    print("\n")

if __name__ == "__main__":
    main()
