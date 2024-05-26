import time
from sample_input import *
from settings import *
from GeneticAlgorithm import GeneticAlgorithm
import os

if __name__ == "__main__":
    ga = GeneticAlgorithm(courses, classrooms, population_size, mutation_rate, crossover_rate, elitism_rate)
    ga.create_population()

    #print(os.cpu_count())

    start_time = time.time()
    ga.selection(False)
    end_time = time.time()
    print(f"Time taken to create initial population without multiprocessing: {end_time - start_time} seconds")

    start_time = time.time()
    ga.selection(True)
    end_time = time.time()
    print(f"Time taken to create initial population with multiprocessing: {end_time - start_time} seconds")


