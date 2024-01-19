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


    def add_course(self, course):
        for day, time in course.time_slots:
            self.table[day][time].append(course)
            self.distribution[day][time] += 1
            
    def remove_course(self, course):
        for day, time in course.time_slots:
            for tmp in self.table[day][time]:
                if (tmp.name == course.name):
                    self.table[day][time].remove(tmp)
                    self.distribution[day][time] -= 1

    def find_course_min_indices(self):
        min_value = 9999
        min_i, min_j = (-1, -1)

        for i in range(5):
            for j in range(5):
                if (self.distribution[i][j] > 0 and self.distribution[i][j] < min_value):
                    min_value = self.distribution[i][j]
                    min_i, min_j = i, j

        return min_i, min_j

    
def main():
    classrooms = [
    #Classroom("CR501", 70),
    Classroom("CR502", 65),
    Classroom("CR1", 55),
    Classroom("CR2", 25),
    Classroom("CR4", 45),
    #Classroom("CR3", 30),
    Classroom("CR5", 15),
    Classroom("CR6", 35),
    Classroom("CR7", 35),
    Classroom("CR8", 45),
    ]
    classrooms = sorted(classrooms, key = lambda x : x.capacity) 
    #increasing capacity order

    courses = [
        Course("101", [(1, 1), (3, 2)], 50), 
        Course("102", [(1, 4), (2, 0)], 30), 
        Course("103", [(2, 4), (1, 0)], 40), 
        Course("104", [(3, 0), (2, 2)], 50), 
        Course("105", [(3, 2), (2, 2)], 40), 
        Course("106", [(0, 4), (4, 2)], 50), 
        Course("107", [(0, 3), (3, 1)], 10), 
        Course("108", [(0, 0), (4, 4)], 30), 
        Course("109", [(4, 2), (3, 4)], 30), 
        Course("110", [(3, 4), (2, 3)], 30), 
        Course("111", [(3, 4), (2, 3)], 10), 
        Course("112", [(2, 1), (4, 1)], 30), 
        Course("113", [(2, 0), (4, 3)], 30), 
        Course("114", [(2, 3), (1, 4)], 40), 
        Course("115", [(1, 0), (3, 4)], 10), 
        Course("116", [(3, 2), (1, 1)], 10), 
        Course("117", [(4, 3), (0, 4)], 30), 
        Course("118", [(4, 1), (1, 4)], 10), 
        Course("119", [(1, 0), (1, 1)], 10), 
        Course("120", [(3, 0), (1, 0)], 40), 
    ]
    schedule = Schedule()

    for course in courses:
        schedule.add_course(course)


    for i in range(5):
        for j in range(5):
            schedule.table[i][j] = sorted(schedule.table[i][j], key = lambda x : x.capacity)

    final_result = [] #list of assigned courses

    ok = False
    while (not ok):
        min_i, min_j = schedule.find_course_min_indices()
        if (min_i == -1 and min_j == -1):
            ok = True
            break

        course = schedule.table[min_i][min_j][0]

        for classroom in classrooms:
            if (classroom.status[min_i][min_j] == 0 and classroom.capacity >= course.capacity):

                #assign course and classroom
                classroom.status[min_i][min_j] = course
                course.room = classroom
                course.slot = (min_i, min_j)
                final_result.append(course)
            
                #mark course as processed and remove from distribution
                schedule.remove_course(course)

                break

    for course in final_result:
        print(f"{course.name}: {course.room.name}, {course.slot}")
    
    classrooms = sorted(classrooms, key = lambda x : x.name)
    
    for classroom in classrooms:
        print(f"{classroom.name}:")
        for i in range(5):
            for j in range(5):
                if (classroom.status[i][j] != 0):
                    print(f"Day {i}, Time slot {j}: Course {classroom.status[i][j].name}")

main()