from abc import ABC, abstractmethod
from people_data import PeopleData

class User(ABC, PeopleData):
    @abstractmethod
    def get_info(self):
        pass