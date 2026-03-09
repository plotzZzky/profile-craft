import random


class TelephoneCreator:
    ddd: str = ""
    telephones: list = []

    def create_new_telephone_list(self, ddd: str):
        self.telephones = []
        self.ddd = ddd
        length: int = random.randrange(1, 4)

        while len(self.telephones) < length:
            telephone: str = self.create_new_telephone()
            self.telephones.append(telephone)

        return self.telephones

    def create_new_telephone(self) -> str:
        phone: str = ""

        for _ in range(1, 9):
            n: str = str(self.receive_random_number())
            phone = phone + n

        return self.format_phone_number(phone)

    def format_phone_number(self, number: str) -> str:
        extra_number = random.choice(["", 9]) # Adiciona o 9 na frente para celulares
        formated_number: str = f"({self.ddd}){extra_number}{number[:4]}-{number[4:]}"

        return formated_number

    @staticmethod
    def receive_random_number():
        number: int = random.randrange(0, 9)
        return number
