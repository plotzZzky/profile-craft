from creators.generic_creator import GenericCreator
from creators.name import NameCreator
from creators.email import EmailCreator
import json


name_creator = NameCreator()
email_creator = EmailCreator()


class BasicPerson(GenericCreator):
    def __init__(self, female: bool | None = None):
        # Creators
        self._name_creator = name_creator
        self.email_creator = email_creator

        # Personal data
        self.female: bool = self._select_true_or_false(female)
        self.name: str = ""
        self.father_lastname: str = ""
        self.mother_lastname: str = ""
        self.emails: list = []

    def create_new_person(self):
        """ Cria as informações de uma nova pessoa """
        # Personal data
        self.name: str = self._name_creator.return_random_name(female=self.female)
        self.father_lastname: str = self._name_creator.return_lastname()
        self.mother_lastname: str = self._name_creator.return_lastname()

        self.emails: list = self.email_creator.return_email_list(self.name, self.father_lastname, self.father_lastname)

    def serialize_me(self) -> dict:
        self.create_new_person()

        return {
            "name": self.name,
            "father_lastname": self.father_lastname,
            "mother_lastname": self.mother_lastname,
            "emails": self.emails,
        }

    def show_result(self) -> dict:
        me: dict = self.serialize_me()
        print(json.dumps(me, indent=4, ensure_ascii=False))

        return me
