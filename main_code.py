from sample_input import *
from settings import *
from GeneticAlgorithm import GeneticAlgorithm

ga = GeneticAlgorithm(courses, classrooms, population_size, mutation_rate, crossover_rate, elitism_rate)

ga.create_population()

print("Generation: ", 0, " best fitness: ", ga.population[0].fitness)

original_population_size = population_size

with open("log.txt", "w") as log:
    for i in range(101):
        population_size = original_population_size + i*50
        ga = GeneticAlgorithm(courses, classrooms, population_size, mutation_rate, crossover_rate, elitism_rate)
        ga.create_population()
        print("New population size")
        while True:
            ga.selection()
            avg_10_percent_fitness = 0
            for j in range(int(population_size/10)):
                avg_10_percent_fitness += ga.population[j].fitness

            # print(ga.population[0].classroom_penalty, ga.population[0].course_penalty, ga.population[0].fitness)
            avg_10_percent_fitness /= int(population_size / 10)
            avg_10_percent_fitness = round(avg_10_percent_fitness, 3)
            if avg_10_percent_fitness >= -5:
                log.write("Decent solutions found. Best fitness: ")
                for j in range(10):
                    log.write(str(ga.population[j].fitness))
                    log.write(" ")
                log.write("\n")
                break


            print(ga.previous_best_fitness)

            if ga.previous_best_fitness >= avg_10_percent_fitness:
                ga.no_improvement_counter += 1
            else:
                ga.no_improvement_counter = 0  # Reset the counter if there's improvement
            # print(ga.no_improvement_counter)
            # If there's no improvement for 100 continuous generations, stop the algorithm
            if ga.no_improvement_counter >= 10:
                log.write("No improvement. Best fitness: ")
                for j in range(10):
                    log.write(str(ga.population[j].fitness))
                    log.write(" ")
                log.write(str(avg_10_percent_fitness))
                log.write("\n")
                break

            ga.previous_best_fitness = max(ga.previous_best_fitness, avg_10_percent_fitness)  # Update the best fitness





"""OUTPUT"""
res = [[["" for _ in range(len(classrooms))] for _ in range(6)] for _ in range(5)]


time_in_day = ["8AM", "9:45AM", "11:30AM", "1:15PM", "3PM", "4:45PM"]

for i in range(len(courses)):
    chosen_slot = courses[i].time_slots[ga.population[0].time[i]]
    chosen_room = ga.population[0].room[i]
    for chosen_day, chosen_time, _ in chosen_slot:
        res[chosen_day][chosen_time][chosen_room] += courses[i].name
    if len(chosen_slot) == 1:
        if chosen_slot[0][1] == 5:
            print("error", courses[i].name)
        res[chosen_slot[0][0]][chosen_slot[0][1] + 1][chosen_room] += courses[i].name

with open("output.txt", "w") as f:
    for day in range(5):
        f.write(" ")
        for i in range(len(classrooms)):
            f.write(classrooms[i].name + ("row" if i == len(classrooms) - 1 else " "))
        for i in range(6):
            f.write(time_in_day[i] + " ")
            for j in range(len(classrooms)):
                f.write((res[day][i][j] if res[day][i][j] != "" else "_")
                        + ("row" if j == len(classrooms) - 1 else " "))
        f.write("end\n")
