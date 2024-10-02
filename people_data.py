import re
from datetime import datetime

class PeopleData:
    _id_counter = 1

    def __init__(self, first_name, last_name, email, phone_number, date_of_birth):
        self._id = PeopleData._generate_id()
        self._first_name = self.validate_name(first_name)
        self._last_name = self.validate_name(last_name)
        self._email = self.validate_email(email)
        self._phone_number = self.validate_phone_number(phone_number)
        self._date_of_birth = self.validate_date_of_birth(date_of_birth)

    @classmethod
    def _generate_id(cls):
        current_id = cls._id_counter
        cls._id_counter += 1
        return current_id

    @property
    def id(self):
        return self._id

    @staticmethod
    def validate_name(name):
        if name.isalpha():
            return name
        raise ValueError("Ім'я та прізвище повинні складатися тільки з букв.")

    @staticmethod
    def validate_email(email):
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if re.match(email_regex, email):
            return email
        raise ValueError("Невірний формат email.")

    @staticmethod
    def validate_phone_number(phone_number):
        if phone_number.isdigit() and len(phone_number) in [10, 12]:
            return phone_number
        raise ValueError("Номер телефону повинен складатися тільки з цифр та мати 10 або 12 символів.")

    @staticmethod
    def validate_date_of_birth(date_of_birth):
        try:
            return datetime.strptime(date_of_birth, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("Дата народження повинна бути у форматі РРРР-ММ-ДД.")

    @staticmethod
    def validate_position_or_workplace(value):
        if all(c.isalpha() or c.isspace() for c in value):
            return value
        raise ValueError("Посада та місце роботи повинні складатися тільки з букв і пробілів.")

    def get_full_name(self):
        return f"{self._first_name} {self._last_name}"

    def get_full_info(self):
        return (
            f"ID: {self._id}, Ім'я: {self._first_name}, Прізвище: {self._last_name}, "
            f"Email: {self._email}, Телефон: {self._phone_number}, Дата народження: {self._date_of_birth}"
        )

    def update_contact_info(self, update_choice, new_value):
        if update_choice == "email":
            self._email = self.validate_email(new_value)
        elif update_choice == "phone_number":
            self._phone_number = self.validate_phone_number(new_value)
        return "Контактну інформацію оновлено."
