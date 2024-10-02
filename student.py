from user import User
from datetime import datetime

class Student(User):
    def __init__(self, first_name, last_name, email, phone_number, date_of_birth, year_of_admission, institute, department):
        User.__init__(self, first_name, last_name, email, phone_number, date_of_birth)
        self._year_of_admission = self.validate_year_of_admission(year_of_admission)
        self._institute = institute
        self._department = department
        self._enrollments = []

    @staticmethod
    def validate_year_of_admission(year):
        current_year = datetime.now().year
        if isinstance(year, int) and 1900 <= year <= current_year:
            return year
        raise ValueError("Рік вступу повинен бути коректним числом у межах 1900 і поточного року.")

    def enroll(self, course):
        self._enrollments.append(course)

    def drop_course(self, course_name):
        self._enrollments = [e for e in self._enrollments if e != course_name]
        return f"Курс {course_name} видалено."

    def get_enrollments(self):
        return f"Записано на курси: {', '.join(self._enrollments)}" if self._enrollments else "Немає записів на курси."

    def get_total_courses(self):
        return f"Загальна кількість курсів: {len(self._enrollments)}"

    def get_info(self):
        return (
            f"{self.get_full_info()}, Інститут: {self._institute}, "
            f"Кафедра: {self._department}, Рік вступу: {self._year_of_admission}"
        )
