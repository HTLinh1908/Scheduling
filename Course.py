from Classroom import Classroom
class Course:

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

