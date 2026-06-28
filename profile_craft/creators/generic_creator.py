import random
import json


class GenericCreator:

    @staticmethod
    def _open_txt_list(filename: str):
        with open(filename, "r") as file:
            return [line.strip() for line in file.readlines()]

    @staticmethod
    def _open_json_list(filename: str):
        with open(filename, "r") as file:
            return json.load(file)

    @staticmethod
    def _return_random_number():
        number: int = random.randrange(0, 9)
        return number

    @staticmethod
    def _select_random_number_in_list():
        number_range = list(range(0, 99))
        number_list = ["", *number_range]
        return random.choice(number_list)

    @staticmethod
    def _select_random_choice_in_list(options: list):
        return random.choice(options)

    def _select_true_or_false(self, value: bool | None) -> bool:
        if type(value) != bool:
            return self._select_random_choice_in_list([True, False])

        else:
            return bool(value)
