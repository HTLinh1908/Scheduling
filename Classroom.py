import numpy as np

class Classroom():
    DaysOfTheWeekEncoded = { 0:'Monday', 1:'Tuesday', 2:'Wednesday', 3:'Thursday', 4:'Friday'}

    def __init__(self, room, capacity, amenity, priority, building):
        self.room = room
        self.status_encoded = np.array([np.zeros(5)]*23)
        self.type = type
        self.status = [[] * 6] * 23
        self.amenity = amenity
        self.building = building

    def set_amenity(self, amenity): self.amenity = amenity
    
    def set_priority(self, priority): self.priority = priority

    def set_status(self):
        for i in range(6):
            self.status[1,i]=DaysOfTheWeekEncoded.get(i)

    def is_free(self, day, start, finish):
        free = True
        for index in range(start,finish):
            if self.status_encoded(day,index) ==1:
                free = False
        return free

    def set_busy(self, day, start, finish):
        if self.check_if_free(self,day,start,finish)==True:
            self.status_encoded[day,start,finish]=1
            return True
        return False
class Course:
    def __init__(self, name, department, type, instructor, max_number_of_student, credit, amenity):
        self.name = name
        self.department = department
        self.type = type
        self.instructor = instructor
        self.max_number_of_student = max_number_of_student
        self.credit = credit
        self.amenity = amenity

class Department:
    def __init__(self, name, course):
        self.name = name
        self.course = course
    
    def get_name(self): return self.name

    def get_course(self): return self.course

class Instructor:
    def __init__(self, name): self.name = name
    def get_name(self): return self.name

class Class:
    def __init__(self, department, course):
        self.department = department
        self.course = course
        self.instructor = None
        self.room = None
    
    def get_department(self): return self.department

    def get_course(self): return self.course

    def get_instructor(self): return self.instructor
    
    def get_room(self): return self.room

    def set_instructor(self, instructor): self.instructor = instructor

    def set_room(self, room): self.room = room
    

class GeneticAlgorithm:
    def evolve(self, population): return self.mutate_population(self.crossover_population(population))

    def crossover_population(self, population):

    def mutate_population(self, population):

       
        