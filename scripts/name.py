from pathlib import Path
import random
import pandas as pd


class CreateName:
    names = []
    lastnames = []

    def return_female_or_male_name(self, gender: bool):
        return self.return_female_name() if gender else self.return_male_name()

    def return_female_name(self):
        self.names = self.generic_open_table(f"female_names.csv")
        return random.choice(self.names)

    def return_male_name(self):
        self.names = self.generic_open_table(f"male_names.csv")
        return random.choice(self.names)

    def return_lastname(self):
        self.lastnames = self.generic_open_table("lastnames.csv")
        return random.choice(self.lastnames)

    @staticmethod
    def generic_open_table(table: str):
        table_path = Path(f"dbs/{table}")
        df = pd.read_csv(table_path, encoding="utf-8", names=["name"])
        result = df['name'].to_list()
        return result
