import random


class Chromosome:
    def __init__(self, courses, classrooms):
        self.fitness = 0
        self.time = [0 for _ in range(len(courses))]
        self.room = [0 for _ in range(len(courses))]
        self.classrooms = classrooms
        self.courses = courses
        self.classroom_penalty = 0
        self.course_penalty = 0

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

        # weights of each constraint
        course_penalty_weight = 1
        classroom_penalty_weight = 0

        # evaluate the goodness of the classroom assignment
        self.classroom_penalty = 0
        # for i in range(len(self.courses)):
        #     if self.courses[i].capacity > self.classrooms[self.room[i]].capacity:
        #         self.classroom_penalty -= course_penalty_weight
        #     else:
        #         self.classroom_penalty -= classroom_penalty_weight*(self.classrooms[self.room[i]].capacity - self.courses[i].capacity)

        for i in range(len(self.courses)):
            if self.courses[i].capacity > self.classrooms[self.room[i]].capacity:
                self.classroom_penalty -= classroom_penalty_weight

        # check if there is two courses in the same room at the same time slot
        m = [[[0 for _ in range(len(self.classrooms))] for _ in range(6)] for _ in range(5)]
        self.course_penalty = 0

        for i in range(len(self.courses)):
            chosen_slot = self.courses[i].time_slots[self.time[i]]
            chosen_room = self.room[i]
            for chosen_day, chosen_time, _ in chosen_slot:
                m[chosen_day][chosen_time][chosen_room] += 1

                if m[chosen_day][chosen_time][chosen_room] > 1:
                    self.course_penalty -= course_penalty_weight

            # 3-hour course
            if len(chosen_slot) == 1:
                m[chosen_slot[0][0]][chosen_slot[0][1] + 1][chosen_room] += 1
                if m[chosen_slot[0][0]][chosen_slot[0][1] + 1][chosen_room] > 1:
                    self.course_penalty -= course_penalty_weight

        self.fitness = self.classroom_penalty + self.course_penalty
