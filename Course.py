import numpy as np
from Classroom import Classroom
class Course:
    room = ""
    slot = (-1, -1)

    def __init__(self, name, time_slots, capacity):
        self.name = name
        # the course code, E.g. CS302, MATH101

        self.time_slots = time_slots
        # 3 possible time slots, each time slot is represented by
        # a list of a tuple class time information: (day_i, starting time_i, duration_i)
        # Example for one preferred time slot: [(0, 8, 1.5), (2, 8, 1.5)]
        # means the course first preferred time slot is Monday and Wednesday from 8:00 to 9:30
        # The same applies for the second and third preferred time slots.

        self.capacity = capacity

    def get_timeslots(self, index):
        return self.time_slots[index]

    def get_capacity(self):
        return self.capacity

    def get_name(self):
        return self.name


def timeslots_matrix(timeslot_list):
    matrix = np.zeros((5, 6))
    for i in timeslot_list:
        if i[0][2] == 1.5:
            matrix[i[0][0], i[0][1]] += 1
            matrix[i[0][0]+2, i[0][1]] += 1
        if i[0][2] == 3:
            matrix[i[0][0], i[0][1]] += 1
            matrix[i[0][0], i[0][1]+1] += 1
    return matrix

def filter_timeslots(list_of_course, chromosome):
    timeslots_list = []
    chromosome_list = [int(i) for i in list(chromosome)]
    index = 0
    for element in list_of_course:
        timeslots_list.append(element.get_timeslots(chromosome_list[index]))
        index += 1
    return timeslots_list

def check_overlapped(list_of_course, chromosome):
    timeslots_list = filter_timeslots(list_of_course, chromosome)
    penalty = 0

    if np.any(timeslots_matrix(timeslots_list) > 1):
        penalty += 1000

    return penalty





def check_availability(list_of_course, chromosome, list_of_classroom):
    classroom_capacity = []
    course_capacity_matrix = []
    for element in list_of_classroom:
        classroom_capacity.append(element.get_capacity())
    timeslots_list = filter_timeslots(list_of_course, chromosome)


def capacity_matrix(list_of_course, chromosome, list_of_classroom):
    global classrooms
    matrix = np.zeros((5, 6, len(classrooms)))
    classroom_capacity = []
    for room in list_of_classroom:
        classroom_capacity.append(room.get_capacity())


courses = [
    Course("101", [[(0, 0, 1.5), (2, 0, 1.5)], [(0, 0, 1.5), (2, 0, 1.5)], [(1, 2, 1.5), (3, 2, 1.5)]], 20),
    Course("102", [[(0, 0, 3)], [(0, 0, 3)], [(4, 1, 3)]], 20),
    Course("103", [[(0, 0, 1.5), (3, 2, 1.5)], [(1, 3, 1.5), (3, 3, 1.5)], [(0, 3, 1.5), (2, 3, 1.5)]], 40),
    Course("104", [[(0, 0, 1.5), (3, 2, 1.5)], [(0, 3, 1.5), (2, 3, 1.5)], [(0, 3, 1.5), (2, 3, 1.5)]], 30),
    Course("105", [[(0, 0, 1.5), (2, 2, 1.5)], [(1, 3, 1.5), (3, 3, 1.5)], [(1, 1, 1.5), (3, 1, 1.5)]], 30),
]
classrooms = [
    Classroom("CR501", 70),
    Classroom("CR502", 65),
    Classroom("CR1", 55),
    Classroom("CR2", 25),
    Classroom("CR4", 45),
    Classroom("CR3", 30),
    Classroom("CR5", 15),
    Classroom("CR6", 35),
    Classroom("CR7", 35),
    Classroom("CR8", 45),
]
classrooms = sorted(classrooms, key = lambda x : x.capacity)

print(check_overlapped(courses, '00000'))



#print(check_overlapped(courses, '00000'))