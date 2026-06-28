from persons.basic_person import BasicPerson
from persons.full_person import FullPerson


class CouplePerson(BasicPerson):
    partner: dict = {}
    me: dict = {}

    def __init__(self, female: bool | None = None, father_lastname: str = "", mother_lastname: str = "", age_group: str = "adult"):
        super().__init__()
        self.female: bool | None = female
        self.father_lastname: str | None = father_lastname
        self.mother_lastname: str | None = mother_lastname
        self.age_group: str = age_group

    def create_new_person(self):
        me = FullPerson(self.female, self.father_lastname, self.mother_lastname, self.age_group)
        self.me: dict = me.serialize_me()

    def create_relationship(self):
        if self.me['relationship'] in ["Namorando(a)", "Noivo(a)", "Casado(a)"]:
            # Cria um parceiro aleatorio na mesma faixa etaria
            partner = FullPerson(None, None, None, self.age_group)
            self.partner: dict = partner.serialize_me()

            # Adiciona o relacionamento a pessoa
            self.me["relationship"] = {"status": self.me["relationship"], "partner": self.partner}

    # Serializers
    def serialize_me(self):
        self.create_new_person()
        self.create_relationship()
        return self.me
