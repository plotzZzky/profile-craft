from persons.basic_person import BasicPerson
from persons.hereditary_person import HereditaryPerson
from persons.couple_person import CouplePerson


# Basic persons
def create_n_basic_persons(rounds: int = 1, female: bool = False) -> list:
    return generic_create_n_person(
        BasicPerson(female).show_result,
        rounds,
    )


def create_n_female_basic_persons(rounds: int = 1) -> list:
    return create_n_basic_persons(rounds, True)


def create_n_male_basic_persons(rounds: int = 1) -> list:
    return create_n_basic_persons(rounds, False)


# Full persons
def create_n_full_person(rounds: int = 1, female: bool = False) -> list:
    return generic_create_n_person(
        CouplePerson(female).show_result,
        rounds
    )


def create_n_female_full_person(rounds: int = 1) -> list:
    return create_n_full_person(rounds, True)


def create_n_male_full_person(rounds: int = 1) -> list:
   return create_n_full_person(rounds, False)


# Hereditary person
def create_n_hereditary_person(rounds: int = 1, female: bool = False) -> list:
    return generic_create_n_person(
        HereditaryPerson(female).show_result,
        rounds
    )


def create_n_hereditary_female_person(rounds: int = 1) -> list:
    return create_n_hereditary_person(rounds, True)


def create_n_hereditary_male_person(rounds: int = 1) -> list:
    return create_n_hereditary_person(rounds, False)


# Generic function
def generic_create_n_person(func, rounds: int = 1) -> list:
    """ Função basica para ser usada na api """
    persons_list: list = []

    for _ in range(0, rounds):
        persons_list.append(func())

    return persons_list


# Run from api
if __name__ == "__main__":
    create_n_male_full_person()
