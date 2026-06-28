from pathlib import Path
import json, sys


class MenuBase:
    APP_DESC: str = "Gerador de perfis sintéticos para testes de aplicações e simulações de dados\n"
    menu_options: list = []

    # Jsons e lists
    ufs: dict = []
    person_uf_json: dict = {}
    persons_list: list = []


    def welcome(self):
        name: str = self.__class__.__name__ # ProfileCraft

        try:
            import art
            art.tprint(name)

        except ModuleNotFoundError:
            # Se o art não tiver disponivel usa o print
            print(f"{' ' * 27}{name}")

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
            self.exit_menu_cli()

    def receive_amount_of_persons(self):
        """ Verifica quantos perfis criar """
        try:
            amount: int = int(input("\nQuantos perfis você deseja criar? "))
            return amount

        except (ValueError, TypeError):
            print("Valor invalido!")
            self.receive_amount_of_persons()

    def save_person_in_json_file(self):
        self.check_and_create_results_folder()
        filename = self.return_filename_to_save_json()

        with open(f"results/persons{filename}.json", "w", encoding="utf-8") as file:
            json.dump(self.persons_list, file, indent=4, ensure_ascii=False)

    def return_filename_to_save_json(self) -> str:
        """ Retorna o nome das pessoas criadas para ser usado no nome do json """
        names = ""

        # Seleciona o nome das pessoas criadas nessa rodada
        for person in self.persons_list[:3]:
            names = names + f"_{person['name'].lower()}"

        return names

    @staticmethod
    def check_and_create_results_folder():
        # Cria a pasta results se ela não existir
        results_path: Path = Path("results/")

        if not results_path.exists():
            results_path.mkdir()

    def generic_menu_function(self, func):
        """ Função generica para executar o menus """
        self.persons_list = func() # recebe a lista de pessoas da função da api
        self.menu_check_if_save_json()

    def menu_check_if_save_json(self):
        choice: str = input("\nSalvar como json na pasta results?(Y/N) ")

        if choice.lower() == "y":
            self.save_person_in_json_file()

        self.show_menu_options()

    @staticmethod
    def exit_menu_cli():
        print("\nBye!")
        sys.exit()
