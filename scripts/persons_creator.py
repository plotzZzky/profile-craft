from .name import CreateName
from .cpf import CpfCreator
from .email import EmailCreator
from .telephone import TelephoneCreator
from .jobs import JobCreator
from .birthday import BirthdayCreator
from .relationship import RelationshipCreator
from pathlib import Path
import random
import json


class PersonCreator:
    """ Classe responsavel por criar as personas """

    # Creators
    create_name = CreateName()
    create_cpf = CpfCreator()
    create_email = EmailCreator()
    create_phone = TelephoneCreator()
    create_job = JobCreator()
    create_birthday = BirthdayCreator()
    create_relationship = RelationshipCreator()

    # Jsons e lists
    ufs: dict = []
    person_uf_json: dict = {}
    persons_list: list = []

    def __init__(self):
            self.open_ufs_json()

    def open_ufs_json(self):
        """ Importa a lista com todos os estados """
        with open("dbs/ufs.json", "r", encoding="utf-8") as file:
            self.ufs = json.load(file)

    # Create n persons
    @staticmethod
    def _generic_create_n_persons(func, func2=None):
        """
            Cria n perfis diferentes
            Args:
                 - Func - Função do tipo de perfil a ser criado
                 - Func2 - Se tiver dois possiveis perfils (homem e mulher)
        """
        choice: str = input("\nQuantos perfis criar: ")

        for _ in range(0, int(choice)):
            if not func2:
                func()
            else:
                random.choice([func, func2])()

    # Hereditary
    def generic_create_hereditary_person(self, gender = None):
        if not gender:
            gender = random.choice([True, False])

        mother = self.create_mother_person_json()
        father = self.create_father_person_json()
        child = self.create_children_person_json(gender=gender, father=father, mother=mother)

        self.persons_list.append(child)

    def create_children_person_json(self, gender, father, mother):
        self.create_birthday.create_young_birthday()
        person = self.return_full_person_json(gender=gender, father=father, mother=mother)
        person["lastname"] = father["lastname"] # recebe o sobrenome do pai
        person["second_lastname"] = mother["lastname"] # recebe o sobrenome da mãe

        return person

    def create_father_person_json(self):
        self.create_birthday.create_elderly_birthday()
        return self.return_full_person_json(gender=False, parents=True)

    def create_mother_person_json(self):
        self.create_birthday.create_elderly_birthday()
        return self.return_full_person_json(gender=True, parents=True)

    def create_aleatory_person_json(self):
        choice: bool = random.choice([True, False])
        return self.return_full_person_json(gender=choice, partner=True)

    # Jsons
    def return_simple_person_json(self, gender: bool):
        name, lastname, second_lastname, email = self.return_name_lastname_email(gender)

        return {
        "name": name,
        "lastname": lastname,
        "second_lastname": second_lastname,
        "email": email[0] # Retorna so o primeiro email da lista
        }

    def return_full_person_json(self,
        gender: bool = False, father: dict = None, mother: dict = None, parents: bool = False, partner: bool = True
    ):
        """ Retorna um perfil completo """
        name, lastname, second_lastname, email = self.return_name_lastname_email(gender)
        person_uf, state, city, telephone = self.return_uf_state_city_phone()
        relationship = self.create_relationship.return_relationship(parents)

        person_json = {
        "cpf": self.create_cpf.return_new_cpf(self.person_uf_json['code']),
        "name": name,
        "lastname": lastname,
        "second_lastname": second_lastname,
        "birthday": self.create_birthday.check_menu_option_and_return_age(),
        "uf": person_uf,
        "state": state,
        "city": city,
        "job": self.create_job.select_job(person_uf),
        "telephone": telephone,
        "email": email,
        "relationship": relationship,
        }

        if partner and not parents:
            if relationship in ["Namorando(a)", "Noivo(a)", "Casado(a)"]:
                partner = self.return_full_person_json(partner=False)
                person_json["partner"] = partner

        if not partner or parents:
            # Remove o status de relacionamento dos parceiros para evitar bugs
            del person_json["relationship"]

        if father and mother:
            person_json["father"] = father
            person_json["mother"] = mother

        return person_json

    # Utils
    def return_random_uf(self):
        choice = random.choice(list(self.ufs.keys()))
        self.person_uf_json = self.ufs[choice]
        return choice

    def return_name_lastname_email(self, gender: bool = False):
        name = self.create_name.return_female_or_male_name(gender)
        lastname = self.create_name.return_lastname()
        second_lastname = self.create_name.return_lastname()
        email = self.create_email.create_new_email_list(
            name, lastname, second_lastname,
        )

        return name, lastname, second_lastname, email

    def return_uf_state_city_phone(self):
        person_uf = self.return_random_uf()
        state = self.person_uf_json["state"]
        city = self.person_uf_json["city"]
        telephone = self.create_phone.create_new_telephone_list(
            self.person_uf_json['ddd']
        )

        return person_uf, state, city, telephone

    def show_list_of_persons(self):
        """ Exibe o json com todos os perfis """
        self.clean_birthday_age_to_avoid_recreate_bug()
        print("\n", json.dumps(self.persons_list, indent=4, ensure_ascii=False))

    def save_person_json(self):
        self.check_and_create_results_folder()
        filename = self.return_filename_to_save_json()

        with open(f"results/persons{filename}.json", "w", encoding="utf-8") as file:
            json.dump(self.persons_list, file, indent=4, ensure_ascii=False)

    def return_filename_to_save_json(self):
        """ Retorna o nome das pessoas para ser usado no nome do json """
        names = ""

        for person in self.persons_list[:3]:
            names = names + f"_{person['name']}"

        return names

    def clean_birthday_age_to_avoid_recreate_bug(self):
        # Evita o bug ao criar um novo perfil se a idade já foi selecionada no perfil anterior
        self.create_birthday.age = ""

    @staticmethod
    def check_and_create_results_folder():
        # Cria a pasta results se ela não existir
        results_path: Path = Path("results/")

        if not results_path.exists():
            results_path.mkdir()
