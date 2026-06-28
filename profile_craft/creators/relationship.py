from creators.generic_creator import GenericCreator


class RelationshipCreator(GenericCreator):
    adult_options: list = [
        "Solteiro(a)",
        "Namorando(a)",
        "Noivo(a)",
        "Casado(a)",
        "Divorciado(a)",
        "Viuvo(a)",
    ]

    parents_options: list = [
        "Casado(a)",
        "Divorciado(a)",
        "Viuvo(a)",
    ]

    def return_relationship(self, partner, parents: bool = False):
        if parents:
            return self._select_random_choice_in_list(self.parents_options)

        else:
            return  self._select_random_choice_in_list(self.adult_options)
