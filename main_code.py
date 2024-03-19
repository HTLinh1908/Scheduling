from sample_input import *
from settings import *
from GeneticAlgorithm import GeneticAlgorithm

ga = GeneticAlgorithm(courses, classrooms, population_size, mutation_rate, crossover_rate, elitism_rate)

ga.create_population()

print("Generation: ", 0, " best fitness: ", ga.population[0].fitness)

for i in range(1, 101):

    ga.selection()
    print("Generation: ", i, " best fitness: ", ga.population[0].fitness)

