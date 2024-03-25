from sample_input import *
from settings import *
from GeneticAlgorithm import GeneticAlgorithm

ga = GeneticAlgorithm(courses, classrooms, population_size, mutation_rate, crossover_rate, elitism_rate)

ga.create_population()

print("Generation: ", 0, " best fitness: ", ga.population[0].fitness)

for i in range(1, 501):
    ga.selection()
    print("Generation: ", i , " best fitnesses: ", ga.population[0].fitness)
    ##print([x.fitness for x in ga.population])


res = [[["" for _ in range(len(classrooms))] for _ in range(5)] for _ in range(5)]
time_in_day = ["8AM", "9:45AM", "11:30AM", "1:15PM", "3PM"]

for i in range(len(courses)):
    chosen_slot = courses[i].time_slots[ga.population[0].time[i]]
    chosen_room = ga.population[0].room[i]
    for chosen_day, chosen_time, _ in chosen_slot:
        res[chosen_day][chosen_time][chosen_room] += courses[i].name
    if (len(chosen_slot) == 1):
        res[chosen_slot[0][0]][chosen_slot[0][1] + 1][chosen_room] += courses[i].name

with open("output.txt", "w") as f:
    for day in range(5):
        f.write(" ")
        for i in range(len(classrooms)):
            f.write(classrooms[i].name + ("row" if i == len(classrooms) - 1 else " "))
        for i in range(5):
            f.write(time_in_day[i] + " ")
            for j in range(len(classrooms)):
                f.write((res[day][i][j] if res[day][i][j] != "" else "_") + ("row" if j == len(classrooms) - 1 else " "))
        f.write("end\n")


