from creators.generic_creator import GenericCreator


class StateCreator(GenericCreator):
    ufs: dict = {}

    def __init__(self):
        self.ufs: dict = self._open_json_list("data/ufs.json")

    def return_random_state(self):
        uf = self.return_random_uf()
        state = self.ufs[uf]["state"]
        city = self._select_random_choice_in_list(self.ufs[uf]["cities"])

        return {"uf": uf, "state": state, "city": city}

    def return_random_uf(self):
        choice = self._select_random_choice_in_list(list(self.ufs.keys()))
        return choice
