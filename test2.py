import numpy as np


class Classroom():
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.status = [[0 for _ in range(5)] for _ in range(5)] 
        #print(self.status)

class Course():
    room = ""
    slot = (-1, -1)
    def __init__(self, name, time_slots, capacity):
        self.name = name 
        #the course code, E.g. CS302, MATH101

        self.time_slots = time_slots 
        # 3 possible time slots, each is a tuple (day, starting time), 
        # assumed that each course is 1h30m long

        self.capacity = capacity

class Schedule():
    
    table = [[[] for _ in range(5)] for _ in range(5)] 
    distribution = [[0 for j in range(5)] for i in range(5)]


    def add_course_1h30x2(self, course):
        for day, time in course.time_slots:
            self.table[day][time].append(course)
            self.distribution[day][time] += 1
            self.table[day+2][time].append(course)
            self.distribution[day+2][time] += 1

    def find_course_min_indices(self):
        min_value = 9999
        min_i, min_j = (-1, -1)

        for i in range(5):
            for j in range(5):
                if (self.distribution[i][j] > 0 and self.distribution[i][j] < min_value):
                    min_value = self.distribution[i][j]
                    min_i, min_j = i, j

        return min_i, min_j

    def remove_course_1h30x2(self, course):
        for day, time in course.time_slots:
            for tmp in self.table[day][time]:
                if (tmp.name == course.name):
                    self.table[day][time].remove(tmp)
                    self.distribution[day][time] -= 1
                    self.table[day+2][time].remove(tmp)
                    self.distribution[day+2][time] -= 1

nigga = 12345
print(nigga)
