import numpy as np
from Chromosome import Chromosome
class GeneticAlgorithm():
    def __init__(self, courses, classrooms, population_size, mutation_rate, crossover_rate, elitism_rate):
        self.population = []
        self.courses = courses
        self.classrooms = classrooms
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.elitism_rate = elitism_rate
        self.best_individuals = []

    def create_population(self):
        self.population = []
        for _ in range(self.population_size):
            new_chromosome = Chromosome(self.courses)
            new_chromosome.random_generate(self.courses, self.classrooms)
            self.population.append(new_chromosome)
        return self.population

    def selection(self):
        #sort the population by fitness in decreasing order
        self.population.sort(key = lambda x : x.fitness, reverse = True)

        #select the best individuals, the rate is equal elitism_rate
        new_population = self.population[:int(self.elitism_rate*self.population_size)]

        #select the rest of the individuals using tournament selection
        self.population = self.population[int(self.elitism_rate*self.population_size):]
        while len(new_population) < self.population_size:
            parent1 = self.population[np.random.randint(0, len(self.population))]
            parent2 = self.population[np.random.randint(0, len(self.population))]
            child = self.crossover(parent1, parent2)
            child = self.mutation(child)
            child.fitness = child.calculate_fitness(self.courses, self.classrooms)
            new_population.append(child)

    def crossover(self, parent1, parent2):
        #create a new child chromosome
        child = Chromosome(self.courses)

        #for each gene, select randomly from one of the parents
        for i in range(len(parent1.state)):
            if np.random.rand() < self.crossover_rate:
                child.state[i] = parent1.state[i]
            else:
                child.state[i] = parent2.state[i]
        return child

    def mutation(self, individual):
        for i in range(len(individual.state)):
            if np.random.rand() < self.mutation_rate:
                individual.state[i] = np.random.randint(0, len(self.courses[i].time_slots))
        return individual
