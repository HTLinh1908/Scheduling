def Course():
    def __init__(self, name, time_slots, course_capacity):
        self.name = name 
        #the course code, E.g. CS302, MATH101

        self.time_slots = time_slots 
        #3 possible time slots, each is a tuple (day, start time, end time)

        self.course_capacity = course_capacity

    
        