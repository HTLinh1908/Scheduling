import random
class Chromosome():
    def __init__(self, courses):
        self.fitness = 0
        self.state = [0 for _ in range(len(courses))]

    def random_generate(self, courses, classrooms):
        for i in range(len(courses)):
            course = courses[i]
            self.state[i] = random.randint(0, len(course.time_slots) - 1)
        self.fitness = self.calculate_fitness(courses, classrooms)

    def calculate_fitness(self, courses, classrooms):
        pass

    def mutation(self, mutation_rate):
        pass

