from persons.basic_person import BasicPerson
from persons.couple_person import CouplePerson
from persons.full_person import FullPerson


class HereditaryPerson(BasicPerson):
    person_creator = None
    father_person: dict = {}
    mother_person: dict = {}
    me: dict = {}

    def __init__(self, female: bool | None = None):
        super().__init__()
        self.female: bool | None = female
        self.father_creator = FullPerson(False, None, None, "elderly", True)
        self.mother_creator = FullPerson(True, None, None, "elderly", True)

    def create_new_person(self):
        self.father_person: dict = self.father_creator.serialize_me()
        self.mother_person: dict = self.mother_creator.serialize_me()

        self.person_creator = CouplePerson(
            self.female,
            self.father_person['father_lastname'],
            self.mother_person['father_lastname'],
            "adult",
        )
        self.me: dict = self.person_creator.serialize_me()

    # Serializers
    def serialize_me(self):
        self.create_new_person()
        self.me["parents"] = {"father": self.father_person, "mother": self.mother_person}
        return self.me
