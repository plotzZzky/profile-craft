from persons.basic_person import BasicPerson

from creators.cpf import CpfCreator
from creators.name import NameCreator
from creators.birthday import BirthdayCreator
from creators.phone import PhoneCreator
from creators.email import EmailCreator
from creators.jobs import JobCreator
from creators.relationship import RelationshipCreator
from creators.state import StateCreator


cpf_creator = CpfCreator()
name_creator = NameCreator()
birthday_creator = BirthdayCreator()
phone_creator = PhoneCreator()
email_creator = EmailCreator()
job_creator = JobCreator()
state_creator = StateCreator()
relationship_creator = RelationshipCreator()


class FullPerson(BasicPerson):
    def __init__(self,
            female: bool | None = None,
            father_lastname: str | None = "",
            mother_lastname: str | None = "",
            age_group: str = "adult",
            parents: bool = False,
        ):

        # Personal data
        super().__init__(female)
        self._cpf_creator = cpf_creator
        self._name_creator = name_creator
        self._birthday_creator = birthday_creator
        self._job_creator = job_creator
        self._phone_creator = phone_creator
        self._email_creator = email_creator
        self._state_creator = state_creator
        self._relationship_creator = relationship_creator

        self.female: bool = self._select_true_or_false(female)
        self.cpf: str = ""
        self.name: str = ""
        self.father_lastname: str = father_lastname or ""
        self.mother_lastname: str = mother_lastname or ""
        self.age_group = age_group
        self.birthday: str = ""
        self.state: dict = {}

        self.job: str = ""

        self.phones: list = []
        self.emails: list = []

        self.relationship: dict = {}
        self.parents: bool = parents

    def create_new_person(self):
        self.cpf: str = self._cpf_creator.create_new_cpf()
        self.name: str = self._name_creator.return_random_name(self.female)
        self.father_lastname: str = self.father_lastname or self._name_creator.return_lastname()
        self.mother_lastname: str = self.mother_lastname or self._name_creator.return_lastname()
        self.birthday: str = self._birthday_creator.return_random_birthday(self.age_group)

        # Country data
        self.state: dict =  self._state_creator.return_random_state()

        # Job data
        self.job: str = self._job_creator.return_random_job(self.state["uf"])

        # Contact data
        self.phones: list = self._phone_creator.return_phone_list(self.state["city"]["ddd"])
        self.emails: list = self._email_creator.return_email_list(self.name, self.father_lastname, self.mother_lastname)

        # Family data
        if not self.parents:
            self.relationship: dict = self._relationship_creator.return_relationship(False)

    # Serializers
    def serialize_me(self) -> dict:
        self.create_new_person()

        result = {
            "cpf": self.cpf,
            "name": self.name,
            "father_lastname": self.father_lastname,
            "mother_lastname": self.mother_lastname,
            "birthday": self.birthday,
            "state": self.state,
            "phones": self.phones,
            "emails": self.emails,
        }

        if self.relationship:
            result["relationship"] = self.relationship

        return result
