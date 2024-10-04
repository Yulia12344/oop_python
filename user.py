from people_data import PeopleData

class User(PeopleData):
    @property
    def info(self):
        raise NotImplementedError()
