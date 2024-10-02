from student import Student
from worker import Worker


class StudentWorker(Student, Worker):
    def __init__(self, first_name, last_name, email, phone_number, date_of_birth, year_of_admission, position,
                 workplace, institute, department):
        Student.__init__(self, first_name, last_name, email, phone_number, date_of_birth, year_of_admission, institute,
                         department)
        Worker.__init__(self, first_name, last_name, email, phone_number, date_of_birth, position, workplace)

    def get_work_schedule(self):
        return f"{self.get_full_name()} працює на посаді {self._position} у {self._workplace}."

    def get_total_courses(self):
        return f"Студент працює та навчається на {len(self._enrollments)} курсах."

    def get_info(self):
        return f"{Student.get_info(self)}, {Worker.get_work_info(self)}"
