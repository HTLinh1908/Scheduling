import numpy as np
from Chromosome import Chromosome
import multiprocessing as mp
from multiprocessing import Pool, Manager
import time

class GeneticAlgorithm:
    def __init__(self, courses, classrooms, population_size, mutation_rate, crossover_rate, elitism_rate):
        self.population = []
        self.new_population = []
        self.courses = courses
        self.classrooms = classrooms
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.elitism_rate = elitism_rate
        self.best_individuals = []
        self.no_improvement_counter = 0
        self.previous_best_fitness = -999999999

    def create_chromosome(self, _):
        new_chromosome = Chromosome(self.courses, self.classrooms)
        new_chromosome.random_generate()
        new_chromosome.calculate_fitness()
        return new_chromosome

    def create_population(self):
        with Pool(processes=16) as pool:  # Adjust the number of processes as needed
            #print("ok")
            self.population = pool.map(self.create_chromosome, range(self.population_size))
            #print(len(self.population))
        self.population.sort(key=lambda x: x.get_fitness(), reverse=True)
        return self.population

    def create_population_no_multi(self):
        self.population = [self.create_chromosome(_) for _ in range(self.population_size)]
        #print(len(self.population))
        return self.population

    def tournament_selection(self, index):
        parent1 = self.population[np.random.randint(0, len(self.population))]
        parent2 = self.population[np.random.randint(0, len(self.population))]
        child = self.crossover(parent1, parent2)
        child = self.mutation(child)
        child.calculate_fitness()
        # print(child.get_fitness())
        self.new_population[index] = child
        #print(len(self.new_population))
        # print("ok")

    def selection(self, multi):
        # print("performing selection...")
        # sort the population by fitness in decreasing order
        self.population.sort(key=lambda x: x.get_fitness(), reverse=True)
        elitism_cnt = int(self.elitism_rate*self.population_size)
        # select the best individuals, the rate is equal elitism_rate
        self.new_population = self.population

        # select the rest of the individuals using tournament selection
        self.population = self.population[elitism_cnt:]
        cnt = 0
        if (not multi):
            for i in range(elitism_cnt, self.population_size):
                self.tournament_selection(i)
                # print(len(new_population))
        else:
            with Pool(processes=20) as pool:
                pool.map(self.tournament_selection, range(elitism_cnt, self.population_size))
                print("okk")

        self.population = self.new_population
        self.population.sort(key=lambda x: x.get_fitness(), reverse=True)

    def crossover(self, parent1, parent2):
        child = Chromosome(self.courses, self.classrooms)
        for i in range(len(parent1.time)):
            if np.random.rand() < self.crossover_rate:
                child.time[i] = parent1.time[i]
            else:
                child.time[i] = parent2.time[i]
            if np.random.rand() < self.crossover_rate:
                child.room[i] = parent1.room[i]
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
