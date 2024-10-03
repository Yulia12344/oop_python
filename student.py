from user import User
from datetime import datetime


class Student(User):
    def __init__(self, first_name, last_name, email, phone_number, date_of_birth, year_of_admission, institute,
                 department):
        User.__init__(self, first_name, last_name, email, phone_number, date_of_birth)
        self._year_of_admission = self.validate_year_of_admission(year_of_admission)
        self._institute = institute
        self._department = department
        self._enrollments = {}

    @staticmethod
    def validate_year_of_admission(year):
        current_year = datetime.now().year
        if isinstance(year, int) and 1900 <= year <= current_year:
            return year
        raise ValueError("Рік вступу повинен бути коректним числом у межах 1900 і поточного року.")

    def enroll(self, course_name, course_info):
        self._enrollments[course_name] = course_info

    def drop_course(self, course_name):
        if course_name in self._enrollments:
            del self._enrollments[course_name]
            return f"Курс {course_name} видалено."
        return f"Курс {course_name} не знайдено."

    def enrollments(self):
        if not self._enrollments:
            return "Немає записів на курси."
        return "\n".join([f"{course}: {info}" for course, info in self._enrollments.items()])

    def total_courses(self):
        return f"Загальна кількість курсів: {len(self._enrollments)}"

    @User.info.getter
    def info(self):
        return (
            f"{self.full_info}, Інститут: {self._institute}, "
            f"Кафедра: {self._department}, Рік вступу: {self._year_of_admission}"
        )
