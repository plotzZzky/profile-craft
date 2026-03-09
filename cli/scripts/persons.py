from .persons_creator import PersonCreator
import random


class PersonMenu(PersonCreator):
    """ Classe responsavel por criar as pessoas """

    # Simple person
    def _create_simple_female_person(self):
        self.persons_list.append(
            self.return_simple_person_json(gender=True)
        )

    def _create_simple_male_person(self):
        self.persons_list.append(
            self.return_simple_person_json(gender=False)
        )

    # Full person
    def _create_full_female_person(self):
        self.persons_list.append(
            self.return_full_person_json(gender=True)
        )

    def _create_full_male_person(self):
        self.persons_list.append(
            self.return_full_person_json(gender=False)
        )

    def _create_full_aleatory_person(self):
        self.persons_list.append(
            self.create_aleatory_person_json()
        )

    # Cria varios perfis
    def _create_n_persons_female(self):
        self._generic_create_n_persons(
            self._create_full_female_person
        )

    def _create_n_persons_male(self):
        self._generic_create_n_persons(
            self._create_full_male_person
        )

    def _create_n_persons_aleatory(self):
        self._generic_create_n_persons(
            self._create_full_female_person,
            self._create_full_male_person,
        )

    # Hereditary
    def _create_hereditary_female_person(self):
        self.generic_create_hereditary_person(True)

    def create_hereditary_male_person(self):
        self.generic_create_hereditary_person(False)

    def create_hereditary_aleatory_person(self):
        self.generic_create_hereditary_person()

    def _create_n_hereditary_aleatory_person(self):
        self._generic_create_n_persons(
            self.generic_create_hereditary_person
        )
