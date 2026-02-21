import json
import random


class JobCreator:
    jobs: dict = {}

    def __init__(self):
        self.open_jobs_json()

    def open_jobs_json(self):
        with open("dbs/jobs.json", "r") as file:
            self.jobs = json.load(file)

    def select_job(self, uf: str):
        """ Seleciona uma profissão aleatoria na lista de jobs da sua região e estado """
        for region in self.jobs.keys():
            states = self.jobs[region]["states"]

            if uf in states:
                jobs = self.jobs[region]["jobs"]
                return random.choice(jobs)

        return "Desempergado(a)"



