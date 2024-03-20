import random
import numpy as np

class Chromosome():
    def __init__(self, courses, classrooms):
        self.fitness = 0
        self.time = [0 for _ in range(len(courses))]
        self.room = [0 for _ in range(len(courses))]
        self.classrooms = classrooms
        self.courses = courses

    def get_fitness(self):
        return self.fitness

    def random_generate(self):
        for i in range(len(self.courses)):
            course = self.courses[i]
            self.time[i] = random.randint(0, len(course.time_slots) - 1)
            self.room[i] = random.randint(0, len(self.classrooms) - 1)
        self.calculate_fitness()

    def calculate_fitness(self):
        self.fitness = 0

        #check if the course capacity is greater than the classroom capacity
        for i in range(len(self.courses)):
            if self.courses[i].capacity > self.classrooms[self.room[i]].capacity:
                self.fitness -= 1

        #check if there is two courses in the same room at the same time
        for i in range(len(self.courses)):
            for j in range(i+1, len(self.courses)):
                time1 = self.courses[i].time_slots[self.time[i]]
                room1 = self.classrooms[self.room[i]]
                time2 = self.courses[j].time_slots[self.time[j]]
                room2 = self.classrooms[self.room[j]]
                violated = 0
                if (room1.name == room2.name):
                    for k in time1:
                        for t in time2:
                            if k == t:
                                violated = 1
                                break;
                if violated == 1:
                    self.fitness -= 1








