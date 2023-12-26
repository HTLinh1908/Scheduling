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

    
        