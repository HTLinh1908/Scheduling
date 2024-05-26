from Classroom import Classroom
class Course:
    def __init__(self, name, major, level, type, is_restricted, capacity, time_slots = []):
        self.name = name
        # the course code, E.g. CS302, MATH101

        self.major = major
        # the major of the course, E.g. CS, MATH, IS, CORE, etc.

        self.level = level
        # the level of the course: 100, 200, 300

        self.type = type
        # the type of the course: 0 for 1.5h, 1 for 3h

        self.is_restricted = is_restricted
        # a boolean variable to indicate if the course is restricted to a specific time slot

        self.time_slots = time_slots
        # 3 possible time slots, each time slot is represented by
        # a list of a tuple class time information: (day_i, starting time_i, duration_i)
        # Example for one preferred time slot: [(0, 8, 1.5), (2, 8, 1.5)]
        # means the course first preferred time slot is Monday and Wednesday from 8:00 to 9:30
        # The same applies for the second and third preferred time slots.

        self.capacity = capacity

        self.chosen_slot = (-1, -1, -1)

    def get_timeslots(self, index):
        return self.time_slots[index]

    def get_capacity(self):
        return self.capacity

    def get_name(self):
        return self.name

