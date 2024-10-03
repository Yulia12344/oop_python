from user import User
from people_data import PeopleData

class Worker(User):
    def __init__(self, first_name, last_name, email, phone_number, date_of_birth, position, workplace):
        super().__init__(first_name, last_name, email, phone_number, date_of_birth)
        self._position = PeopleData.validate_position_or_workplace(position)
        self._workplace = PeopleData.validate_position_or_workplace(workplace)

    @property
    def work_info(self):
        return f"Посада: {self._position}, Місце роботи: {self._workplace}"

    def update_position(self, new_position, new_workplace):
        self._position = PeopleData.validate_position_or_workplace(new_position)
        self._workplace = PeopleData.validate_position_or_workplace(new_workplace)
        return f"Посада оновлена на {self._position}, Місце роботи оновлено на {self._workplace}"

    @User.info.getter
    def info(self):
        return f"{self.full_info}, {self.work_info}"
