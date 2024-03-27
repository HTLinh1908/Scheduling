from sample_input import *
from settings import *
from GeneticAlgorithm import GeneticAlgorithm

ga = GeneticAlgorithm(courses, classrooms, population_size, mutation_rate, crossover_rate, elitism_rate)

ga.create_population()

print("Generation: ", 0, " best fitness: ", ga.population[0].fitness)

for i in range(1, 1001):
    ga.selection()
    print("Generation: ", i, " best fitness: ", ga.population[0].fitness)
    # print([x.fitness for x in ga.population])

print("Generation: ", 1000, " best fitness: ", ga.population[0].fitness)


def write_output_file(ga, filename):
    res = [[[0 for _ in range(5)] for _ in range(5)]]
    with open(filename, 'w') as f:
        for chromosome in ga.population:
            f.write(' '.join(['CR' + str(room + 1) for room in chromosome.room]) + '\n')
            for i in range(5):  # Assuming there are 5 time slots
                f.write('row')
                for j in range(len(chromosome.time)):
                    if i in chromosome.time[j]:
                        f.write(' ' + str(chromosome.courses[j].id))
                    else:
                        f.write(' _')
                f.write('\n')
            f.write('row end\n')
