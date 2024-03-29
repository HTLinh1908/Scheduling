import numpy as np



class Classroom:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.status = np.zeros((5,6), dtype=int)
        # print(self.status)
    def __str__(self):
        return 'Classroom name: ' + str(self.name) + ' capacity: ' + str(self.capacity) + ' status: ' + str(self.capacity)


class Course:
    room = ""
    slot = (-1, -1)

    def __init__(self, name, time_slots, capacity):
        self.name = name
        # the course code, E.g. CS302, MATH101
        self.time_slots = time_slots
        # 3 possible time slots, each is a tuple (day, starting time), 
        # assumed that each course is 1h30m long

        self.capacity = capacity

    def __str__(self):
        return 'Course name: ' + str(self.name) + ' time_slots: ' + str(self.time_slots) + ' capacity: ' + str(self.capacity)
    def get_time_slots(self):
        return self.time_slots
def update_matrix(arr_list):
    # Initialize the matrix with zeros
    matrix = np.zeros((5, 6))

    # Update the matrix based on the coordinates in arr_list
    for x, y in arr_list:
        if 0 <= x < 5 and 0 <= y < 6:
            matrix[x, y] += 1

        return matrix


def main():
    classrooms = [
        # Classroom("CR501", 70),
        Classroom("CR502", 65),
        Classroom("CR1", 55),
        Classroom("CR2", 25),
        Classroom("CR4", 45),
        # Classroom("CR3", 30),
        Classroom("CR5", 15),
        Classroom("CR6", 35),
        Classroom("CR7", 35),
        Classroom("CR8", 45),
    ]
    classrooms = sorted(classrooms, key=lambda x: x.capacity)
    # increasing capacity order

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

main()
