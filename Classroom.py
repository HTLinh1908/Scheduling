import numpy as np
import random

class Classroom():

    def __init__(self, room, capacity, amenity, priority, building):
        self.room = room
        self.status = np.array([np.zeros(205)])
        self.capacity = capacity
#        self.type = type
#        self.amenity = amenity
#        self.building = building

#    def set_amenity(self, amenity): self.amenity = amenity
    
#    def set_priority(self, priority): self.priority = priority



    def is_free(self, start, finish):
        free = True
        for index in range(start,finish):
            if self.status(index) !=0:
                free = False
        return free

    def set_busy(self, start, finish):
        if self.is_free(self,start,finish)==True:
            self.status[start,finish]=1
            return True
        return False

    def convert_1h30_course(self, day, start, finish):
        return day*41+start, day*41+finish

    def set_busy_1h30x2_course(self, start, finish):
        if self.is_free(self,start,finish)==True and self.is_free(self,start+82,finish+82)==True:
            self.status[start,finish]=1
            self.status(start+82, finish+82)=1
            return True
        return False
class Course:
    def __init__(self, name, number, department, level, instructor, max_number_of_student): #instructor + credit + amenity
        self.name = name
        self.numer = number
        self.department = department
        self.level = level
        self.max_number_of_student = max_number_of_student

    
    def get_name(self): return self.name

    def get_department(self): return self.department

    def get_level(self): return self.level

    def get_instructor(self): return self.instructor

    def get_max_number_of_student(self): return self.max_number_of_student


class Department:
    def __init__(self, department, course):
        self.department = department
        self.course = course
    
    def get_department(self): return self.department

    def get_course(self): return self.course

class Instructor:
    def __init__(self, id, name): 
        self.id= id
        self.name = name
    def get_id(self): return self.id
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

class Schedule:
    def __init__(self):
        pass
