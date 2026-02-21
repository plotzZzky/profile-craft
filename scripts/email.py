import random


class EmailCreator:
    emails_dominions: list = [
        "@mail.com",
        "@mail.com.br",
        "@mail.io",
        "@mail.net",
        "@mail.ia"
        "@edumail.edu",
        "@xmail.com",
    ]

    emails_chars: list = [
        ".",
        "",
        "_",
        "-",
    ]

    emails: list = []
    name: str = ""
    lastname: str = ""
    second_lastname: str = ""

    def create_new_email_list(self, name: str, lastname: str, second_lastname: str):
        self.emails = [] # Limpa a lista de e-mails
        self.name: str = name.lower()
        self.lastname: str = lastname.lower()
        self.second_lastname: str = second_lastname.lower()
        self.generate_email_and_add_to_list()

        return self.emails

    def generate_email_and_add_to_list(self):
        length: int = random.randrange(1, 4)

        while len(self.emails) < length:
            email: str = self.generate_email()

            if email not in self.emails:
                self.emails.append(email)

    def generate_email(self):
        options: list = [
            self.email_name_lastname,
            self.email_lastname_name,
            self.email_initial_name_lastname,
            self.email_lastname_name_lastname,
        ]

        choice = random.choice(options)
        return choice()

    def email_name_lastname(self):
        char: str = random.choice(self.emails_chars)
        lastname: str = random.choice([self.lastname, self.second_lastname])
        dominion: str = random.choice(self.emails_dominions)

        return f"{self.name}{char}{lastname}{dominion}"

    def email_lastname_name(self):
        lastname: str = random.choice([self.lastname, self.second_lastname])
        char: str = random.choice(self.emails_chars)
        dominion: str = random.choice(self.emails_dominions)

        return f"{lastname}{char}{self.name}{dominion}"

    def email_initial_name_lastname(self):
        slice_number: int = random.randrange(1, 5)
        char: str = random.choice(self.emails_chars)
        lastname: str = random.choice([self.lastname, self.second_lastname])
        number: int = self.create_random_number()
        dominion: str = random.choice(self.emails_dominions)

        return f"{self.name[:slice_number]}{char}{lastname}{number}{dominion}"

    def email_lastname_name_lastname(self):
        char: str = random.choice(self.emails_chars)
        dominion: str = random.choice(self.emails_dominions)

        return f"{self.lastname}{char}{self.name}{char}{self.second_lastname}{dominion}"

    @staticmethod
    def create_random_number():
        number_range = list(range(0, 99))
        number_list = ["", *number_range]
        return random.choice(number_list)
