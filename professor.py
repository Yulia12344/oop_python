from user import User

class Professor(User):
    def __init__(self, first_name, last_name, email, phone_number, date_of_birth, academic_title, faculty, institute, department):
        super().__init__(first_name, last_name, email, phone_number, date_of_birth)
        self._academic_title = academic_title
        self._faculty = faculty
        self._institute = institute
        self._department = department
        self._courses = []

    def add_course(self, course_name):
        self._courses.append(course_name)
        return f"Курс {course_name} додано."

    def get_courses(self):
        return f"Курси, які викладає: {', '.join(self._courses)}" if self._courses else "Немає курсів для викладання."

    def get_info(self):
        return (
            f"{self.get_full_info()}, Титул: {self._academic_title}, Факультет: {self._faculty}, "
            f"Інститут: {self._institute}, Кафедра: {self._department}"
        )
