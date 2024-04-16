import numpy as np
from Chromosome import Chromosome


class GeneticAlgorithm:
    def __init__(self, courses, classrooms, population_size, mutation_rate, crossover_rate, elitism_rate):
        self.population = []
        self.courses = courses
        self.classrooms = classrooms
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.elitism_rate = elitism_rate
        self.best_individuals = []
        self.no_improvement_counter = 0
        self.previous_best_fitness = 0

    def create_population(self):
        # print("creating population...")
        self.population = []
        for _ in range(self.population_size):
            new_chromosome = Chromosome(self.courses, self.classrooms)
            new_chromosome.random_generate()
            self.population.append(new_chromosome)
        return self.population

    def selection(self):
        # print("performing selection...")
        # sort the population by fitness in decreasing order
        self.population.sort(key=lambda x: x.get_fitness(), reverse=True)

        # select the best individuals, the rate is equal elitism_rate
        new_population = self.population[:int(self.elitism_rate*self.population_size)]

        # select the rest of the individuals using tournament selection
        self.population = self.population[int(self.elitism_rate*self.population_size):]
        cnt = 0
        while len(new_population) < self.population_size:
            parent1 = self.population[np.random.randint(0, len(self.population))]
            parent2 = self.population[np.random.randint(0, len(self.population))]
            cnt += 1
            child = self.crossover(parent1, parent2, cnt)
            child = self.mutation(child)
            child.calculate_fitness()
            new_population.append(child)
        self.population = new_population
        self.population.sort(key=lambda x: x.get_fitness(), reverse=True)

    def crossover(self, parent1, parent2, cnt):
        child = Chromosome(self.courses, self.classrooms)
        cross_cnt = 0
        for i in range(len(parent1.time)):
            if np.random.rand() < self.crossover_rate:
                child.time[i] = parent1.time[i]
                cross_cnt += 1
            else:
                child.time[i] = parent2.time[i]
            if np.random.rand() < self.crossover_rate:
                child.room[i] = parent1.room[i]
                cross_cnt += 1
            else:
                child.room[i] = parent2.room[i]

        child.calculate_fitness()
        return child

    def mutation(self, chromosome):

        for i in range(len(chromosome.time)):
            if np.random.rand() < self.mutation_rate:
                chromosome.time[i] = np.random.randint(0, len(self.courses[i].time_slots))
            if np.random.rand() < self.mutation_rate:
                chromosome.room[i] = np.random.randint(0, len(self.classrooms))
        chromosome.calculate_fitness()

        return chromosome
