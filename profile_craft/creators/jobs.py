from creators.generic_creator import GenericCreator
import random


class JobCreator(GenericCreator):
    jobs: dict = {}

    def __init__(self):
        self.jobs: dict = self._open_json_list("data/jobs.json")

    def return_random_job(self, uf: str):
        """ Seleciona uma profissão aleatoria na lista de jobs da sua região e estado """
        for region in self.jobs.keys():
            states = self.jobs[region]["states"]

            if uf in states:
                jobs = self.jobs[region]["jobs"]
                return random.choice(jobs)

        return "Desempergado(a)"



