from random import randrange
from datetime import timedelta, datetime


class BirthdayCreator:
    age: str = ""
    start_year = ""
    end_year = ""

    def __init__(self):
        self.options = [
            {"name": "Jovem", "func": self.create_young_birthday},
            {"name": "Adulto", "func": self.create_adult_birthday},
            {"name": "Idoso", "func": self.create_elderly_birthday},
            {"name": "Aleatorio", "func": self.create_elderly_birthday},
        ]

    def show_menu_select_person_age(self):
        print("\nSelecione uma faixa etária:")

        for index, item in enumerate(self.options, 1):
            print(f"{index}- {item['name']}")

    def check_menu_option_and_return_age(self):
        if not self.age:
            self.show_menu_select_person_age()

            try:
                choice = int(input("Selecione uma faixa etaria: "))
                self.options[choice - 1]["func"]()
                return self.age

            except (ValueError, TypeError, IndexError):
                self.check_menu_option_and_return_age()

        else:
            return self.age

    def create_young_birthday(self):
        self.age = self.return_random_date_in_range(
            "1/1/1997", "31/12/2007",
        )

    def create_adult_birthday(self):
        self.age = self.return_random_date_in_range(
            "1/1/1977", "31/12/1996",
        )

    def create_elderly_birthday(self):
        self.age = self.return_random_date_in_range(
            "1/1/1960","31/12/1976",
        )

    def create_random_birthday(self):
        self.age = self.return_random_date_in_range(
            "1/1/1960", "31/12/2007"
        )

    def show_menu_and_receive_new_birthday_date(self):
        return self.check_menu_option_and_return_age() # Colocado aqui para a função retornar a data

    @staticmethod
    def return_random_date_in_range(start, end):
        start_year = datetime.strptime(start, "%d/%m/%Y")
        end_year = datetime.strptime(end, '%d/%m/%Y')

        delta = end_year - start_year
        int_delta = delta.days  # Agora em dias
        random_day = randrange(int_delta)
        random_date = start_year + timedelta(days=random_day)

        # Formata a data para 'DD/MM/YYYY'
        return random_date.strftime('%d/%m/%Y')
