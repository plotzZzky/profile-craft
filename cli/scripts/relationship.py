import random


class RelationshipCreator:
    options: list = [
        "Solteiro(a)",
        "Namorando(a)",
        "Noivo(a)",
        "Casado(a)",
        "Divorciado(a)",
        "Viuvo(a)",
    ]


    def return_relationship(self, parents):
        if not parents:
            return  self.return_children_relationship()

    def return_children_relationship(self):
        return random.choice(self.options)
