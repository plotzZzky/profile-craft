from random import randrange
from datetime import timedelta, datetime


class BirthdayCreator:
    start_year = ""
    end_year = ""

    def __init__(self):
        self.options: dict = {
            "young": self.create_young_birthday,
            "adult": self.create_adult_birthday,
            "elderly": self.create_elderly_birthday,
            "random": self.create_random_birthday,
        }

    def return_random_birthday(self, age_group: str):
        try:
            return self.options[age_group]()

        except KeyError:
            return self.create_random_birthday()

    def create_young_birthday(self):
        return self.return_random_date_in_range(
            "1/1/1997", "31/12/2007",
        )

    def create_adult_birthday(self):
        return self.return_random_date_in_range(
            "1/1/1977", "31/12/1996",
        )

    def create_elderly_birthday(self):
        return self.return_random_date_in_range(
            "1/1/1960","31/12/1976",
        )

    def create_random_birthday(self):
        return self.return_random_date_in_range(
            "1/1/1960", "31/12/2007"
        )

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
