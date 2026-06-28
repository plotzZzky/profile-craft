from creators.generic_creator import GenericCreator
import random


class NameCreator(GenericCreator):
    female_names: list = []
    lastnames: list = []

    def __init__(self):
        self.female_names: list = self._open_txt_list("data/female_names.txt")
        self.male_names: list = self._open_txt_list("data/male_names.txt")
        self.lastnames: list = self._open_txt_list("data/lastnames.txt")

    def return_random_name(self, female: bool = False):
        return self.return_female_name() if female else self.return_male_name()

    def return_female_name(self):
        return random.choice(self.female_names)

    def return_male_name(self):
        return random.choice(self.male_names)

    def return_lastname(self):
        return random.choice(self.lastnames)
