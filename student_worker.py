from student import Student
from user import User
from worker import Worker


class StudentWorker(Student, Worker):
    def __init__(self, first_name, last_name, email, phone_number, date_of_birth, year_of_admission, position,
                 workplace, institute, department):
        Student.__init__(self, first_name, last_name, email, phone_number, date_of_birth, year_of_admission, institute,
                         department)
        Worker.__init__(self, first_name, last_name, email, phone_number, date_of_birth, position, workplace)

    def work_schedule(self):
        return f"{self.full_name} працює на посаді {self._position} у {self._workplace}."

    def total_courses(self):
        return f"Студент працює та навчається на {len(self._enrollments)} курсах."

    @property
    def info(self):
        # we must use fget/fset with parent properties to pass reference to self
        return f"{Student.info.fget(self)}, {Worker.work_info.fget(self)}"
