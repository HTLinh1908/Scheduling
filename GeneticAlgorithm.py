import numpy as np
from Chromosome import Chromosome
class GeneticAlgorithm():
    def __init__(self, courses, classrooms, population_size, mutation_rate, crossover_rate, elitism_rate, max_generations):
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
            new_chromosome.random_generate(self.courses)
            self.population.append(new_chromosome)
        return self.population

    def selection(self, population):
        fitnesses = [chromosome.fitness for chromosome in self.population]
        total_fitness = sum(fitnesses)
        probabilities = [fitness / total_fitness for fitness in fitnesses]
        return np.random.choice(self.population, p=probabilities)

    def crossover(self, parent1, parent2):
        child = []
        for i in range(len(parent1)):
            if np.random.rand() < self.crossover_rate:
                child.append(parent1[i])
            else:
                child.append(parent2[i])
        return child

    def mutation(self, individual):
        for i in range(len(individual)):
            if np.random.rand() < self.mutation_rate:
                individual[i] = self.create_individual()[i]
        return individual

    def elitism(self):
        fitnesses = [self.fitness(individual) for individual in self.population]
        best_individual = self.population[np.argmax(fitnesses)]
        best_fitness = max(fitnesses)
        if best_fitness > self.best