from scripts.persons import PersonMenu
import sys
import art


class ProfileCraft(PersonMenu):
    APP_DESC: str = "Gerador de perfis sintéticos para testes de aplicações e simulações de dados\n"

    def __init__(self):
        super().__init__()

        self.menu_options = [
            {"name": "Criar perfil simples feminino", "func": self.create_one_simple_female_person},
            {"name": "Criar perfil simples masculino", "func": self.create_one_simple_male_person},
            {"name": "Criar perfil completo feminino", "func": self.create_one_full_female_person},
            {"name": "Criar perfil completo masculino", "func": self.create_one_full_male_person},
            {"name": "Criar perfil completo aleatorio", "func": self.create_one_full_aleatory_person},
            {"name": "Criar varios perfis completos femininos", "func": self.create_n_female_persons},
            {"name": "Criar varios perfis completos masculinos", "func": self.create_n_male_persons},
            {"name": "Criar varios perfis completos aleatorios", "func": self.create_n_aleatory_persons},
            {"name": "Criar perfil hereditario feminino", "func": self.create_one_hereditary_female_person},
            {"name": "Criar perfil hereditario masculino", "func": self.create_one_hereditary_male_person},
            {"name": "Criar perfil hereditario aleatorio", "func": self.create_one_hereditary_aleatory_person},
            {"name": "Criar varios perfis hereditario aleatorio", "func": self.create_n_hereditary_aleatory_person},
            {"name": "Sair", "func": self.exit_cli},
        ]

    def welcome(self):
        art.tprint(self.__class__.__name__)
        print(self.APP_DESC)
        self.show_menu_options()

    def show_menu_options(self):
        print(f"{'- ' * 15} Menu {' -' * 15}")

        for index, option in enumerate(self.menu_options, 1):
            print(f"{index}- {option['name']}")

        self.check_menu_option()

    def check_menu_option(self):
        try:
            choice: str = input("\nSelcione uma opção da lista: ")
            self.menu_options[int(choice) - 1]["func"]()

        except (ValueError, TypeError, IndexError) as e:
            print(e)
            self.check_menu_option()

        except KeyboardInterrupt:
            self.exit_cli()

    # Funções para criar os perfis
    def create_one_simple_female_person(self):
        self.generic_menu_function(
            lambda : self._create_simple_female_person()
        )

    def create_one_simple_male_person(self):
        self.generic_menu_function(
            lambda : self._create_simple_male_person()
        )

    def create_one_full_female_person(self):
        self.generic_menu_function(
            lambda : self._create_full_female_person()
        )

    def create_one_full_male_person(self):
        self.generic_menu_function(
            lambda : self._create_full_male_person()
        )

    def create_one_full_aleatory_person(self):
        self.generic_menu_function(
            lambda : self._create_full_aleatory_person()
        )

    def create_n_female_persons(self):
        self.generic_menu_function(
            lambda : self._create_n_persons_female()
        )

    def create_n_male_persons(self):
        self.generic_menu_function(
            lambda : self._create_n_persons_male()
        )

    def create_n_aleatory_persons(self):
        self.generic_menu_function(
            lambda : self._create_n_persons_aleatory()
        )

    def create_one_hereditary_female_person(self):
        self.generic_menu_function(
            lambda : self._create_hereditary_female_person()
        )

    def create_one_hereditary_male_person(self):
        self.generic_menu_function(
            lambda : self.create_hereditary_male_person()
        )

    def create_one_hereditary_aleatory_person(self):
        self.generic_menu_function(
            lambda : self.create_hereditary_aleatory_person()
        )

    def create_n_hereditary_aleatory_person(self):
        self.generic_menu_function(
            lambda : self._create_n_hereditary_aleatory_person()
        )

    # Utils
    def generic_menu_function(self, func):
        self.persons_list: list = [] # limpa a lista

        func() # Função herdada da função pai
        self.show_list_of_persons()
        self.check_if_save_json()

    def check_if_save_json(self):
        choice: str = input("\nSalvar como json na pasta results?(Y/N) ")

        if choice.lower() == "y":
            self.save_person_json()

        self.show_menu_options()

    @staticmethod
    def exit_cli():
        print("\nBye!")
        sys.exit()


profile_craft = ProfileCraft()

if __name__ == "__main__":
    profile_craft.welcome()
