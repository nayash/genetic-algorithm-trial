import numpy as np
from individual import Individual


class Population:
    def __init__(self, target, population_size=10, individuals=None):
        self.gene_set = [0, 1]
        self.population_size = population_size
        if individuals is None:
            self.individuals = [Individual(len(target.get_value())) for i in range(population_size)]
        else:
            if not (population_size == len(individuals)):
                raise Exception("population size and length of individuals passed are different")
            self.individuals = individuals
        self.fitness_scores = []
        self.target = target
        self.calc_fitness_scores()

    @staticmethod
    def calc_fitness_score(individual1, individual2):
        score = 0
        for i1, i2 in zip(individual1.get_value(), individual2.get_value()):
            if i1 == i2:
                score = score + 1
        return score

    def calc_fitness_scores(self):
        for individual in self.individuals:
            self.fitness_scores.append(self.calc_fitness_score(self.target, individual))

    def get_n_best_individual(self, n):
        best_index = np.argsort(self.fitness_scores)[-n]
        return self.individuals[best_index], self.fitness_scores[best_index]

    def add_individual(self, new_individual, fitness_score=-np.inf):
        worst_index = np.argsort(self.fitness_scores)[0]  # least fit individual
        if fitness_score == -np.inf:
            new_individual.set_fitness_score(self.calc_fitness_score(self.target, new_individual))
        self.individuals[worst_index] = new_individual
