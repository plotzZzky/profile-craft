from menus.menu_base import MenuBase
import api


class ProfileCraft(MenuBase):
    def __init__(self):
        self.menu_options = [
            {"name": "Criar perfil simples aleatório", "func": self.menu_create_simple_person},
            {"name": "Criar perfil simples feminino", "func": self.menu_create_simple_female_person},
            {"name": "Criar perfil simples masculino", "func": self.menu_create_simple_male_person},

            {"name": "Criar varios perfis simples aleatório", "func": self.menu_create_n_simple_person},
            {"name": "Criar varios perfis simples feminino", "func": self.menu_create_n_simple_female_person},
            {"name": "Criar varios perfis simples masculino", "func": self.menu_create_n_simple_male_person},

            {"name": "Criar perfil completo aleatorio", "func": self.menu_create_full_person},
            {"name": "Criar perfil completo feminino", "func": self.menu_create_female_full_person},
            {"name": "Criar perfil completo masculino", "func": self.menu_create_male_full_person},

            {"name": "Criar varios perfis completos aleatorios", "func": self.menu_create_n_full_person},
            {"name": "Criar varios perfis completos femininos", "func": self.menu_create_n_female_full_person},
            {"name": "Criar varios perfis completos masculinos", "func": self.menu_create_n_male_full_person},

            {"name": "Criar perfil hereditario aleatorio", "func": self.menu_create_hereditary_person},
            {"name": "Criar perfil hereditario feminino", "func": self.menu_create_hereditary_female_person},
            {"name": "Criar perfil hereditario masculino", "func": self.menu_create_hereditary_male_person},

            {"name": "Criar varios perfis hereditario aleatorio", "func": self.menu_n_create_hereditary_person},
            {"name": "Criar varios perfis hereditario femininos", "func": self.menu_n_create_hereditary_female_person},
            {"name": "Criar varios perfis hereditario masculinos", "func": self.menu_n_create_hereditary_male_person},

            {"name": "Sair", "func": self.exit_menu_cli},
        ]

    # Simple person
    def menu_create_simple_person(self):
        self.generic_menu_function(
            api.create_n_basic_persons
        )

    def menu_create_n_simple_person(self):
        amount: int = self.receive_amount_of_persons()

        self.generic_menu_function(
            lambda: api.create_n_basic_persons(amount)
        )

    def menu_create_simple_female_person(self):
        self.generic_menu_function(
            api.create_n_female_basic_persons
        )

    def menu_create_n_simple_female_person(self):
        amount: int = self.receive_amount_of_persons()

        self.generic_menu_function(
            lambda: api.create_n_female_basic_persons(amount)
        )

    def menu_create_simple_male_person(self):
        self.generic_menu_function(
            api.create_n_male_basic_persons
        )

    def menu_create_n_simple_male_person(self):
        amount: int = self.receive_amount_of_persons()

        self.generic_menu_function(
            lambda: api.create_n_male_basic_persons(amount)
        )

    # Full person
    def menu_create_full_person(self):
        self.generic_menu_function(
            api.create_n_full_person
        )

    def menu_create_n_full_person(self):
        amount: int = self.receive_amount_of_persons()

        self.generic_menu_function(
            lambda: api.create_n_full_person(amount)
        )

    def menu_create_female_full_person(self):
        self.generic_menu_function(
            api.create_n_female_full_person
        )

    def menu_create_n_female_full_person(self):
        amount: int = self.receive_amount_of_persons()

        self.generic_menu_function(
            lambda: api.create_n_female_full_person(amount)
        )

    def menu_create_male_full_person(self):
        self.generic_menu_function(
            api.create_n_male_full_person
        )

    def menu_create_n_male_full_person(self):
        amount: int = self.receive_amount_of_persons()

        self.generic_menu_function(
            lambda: api.create_n_male_full_person(amount)
        )

    # Hereditary person
    def menu_create_hereditary_person(self):
        self.generic_menu_function(
            api.create_n_hereditary_person
        )

    def menu_n_create_hereditary_person(self):
        amount: int = self.receive_amount_of_persons()

        self.generic_menu_function(
            lambda: api.create_n_hereditary_person(amount)
        )

    def menu_create_hereditary_female_person(self):
        self.generic_menu_function(
            api.create_n_hereditary_female_person
        )

    def menu_n_create_hereditary_female_person(self):
        amount: int = self.receive_amount_of_persons()

        self.generic_menu_function(
            lambda: api.create_n_hereditary_female_person(amount)
        )

    def menu_create_hereditary_male_person(self):
        self.generic_menu_function(
            api.create_n_hereditary_male_person
        )

    def menu_n_create_hereditary_male_person(self):
        amount: int = self.receive_amount_of_persons()

        self.generic_menu_function(
            lambda: api.create_n_hereditary_male_person(amount)
        )
