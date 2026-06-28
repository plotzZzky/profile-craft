from creators.generic_creator import GenericCreator
import random


class EmailCreator(GenericCreator):
    emails_dominions: list = []
    emails_chars: list = [".", "", "_", "-"]

    emails: list = []
    name: str = ""
    father_lastname: str = ""
    mother_lastname: str = ""
    email_options: list = []

    def __init__(self):
        self.email_options: list = [
            self.email_name_lastname,
            self.email_lastname_name,
            self.email_initial_name_lastname,
            self.email_lastname_name_lastname,
        ]

        self.emails_dominions: list = self._open_txt_list("data/emails.txt")

    def format_user_data(self, name: str, lastname: str, second_lastname: str):
        self.name: str = name.lower()
        self.father_lastname: str = lastname.lower()
        self.mother_lastname: str = second_lastname.lower()

    def return_email_list(self, name: str, lastname: str, second_lastname: str):
        """ Retorna uma lista de tamanho variavel com os e-mail randomicos """
        self.emails = []  # Limpa a lista de e-mails
        length: int = random.randrange(1, 4)
        self.format_user_data(name, lastname, second_lastname)
        self.generate_new_email_list(length)

        return self.emails

    def generate_new_email_list(self, length):
        while len(self.emails) < length:
            email: str = self.select_random_new_email_func()

            if email not in self.emails:
                self.emails.append(email)

    def select_random_new_email_func(self):
        choice = random.choice(self.email_options)
        return choice()

    # New email functions
    def email_name_lastname(self):
        char: str = random.choice(self.emails_chars)
        lastname: str = random.choice([self.father_lastname, self.mother_lastname])
        dominion: str = random.choice(self.emails_dominions)

        return f"{self.name}{char}{lastname}{dominion}"

    def email_lastname_name(self):
        lastname: str = random.choice([self.father_lastname, self.mother_lastname])
        char: str = random.choice(self.emails_chars)
        dominion: str = random.choice(self.emails_dominions)

        return f"{lastname}{char}{self.name}{dominion}"

    def email_initial_name_lastname(self):
        slice_number: int = random.randrange(1, 5)
        char: str = random.choice(self.emails_chars)
        lastname: str = random.choice([self.father_lastname, self.mother_lastname])
        number: int = self._select_random_number_in_list()
        dominion: str = random.choice(self.emails_dominions)

        return f"{self.name[:slice_number]}{char}{lastname}{number}{dominion}"

    def email_lastname_name_lastname(self):
        char: str = random.choice(self.emails_chars)
        dominion: str = random.choice(self.emails_dominions)

        return f"{self.father_lastname}{char}{self.name}{char}{self.mother_lastname}{dominion}"
