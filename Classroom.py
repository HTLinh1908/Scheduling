import numpy as np
import random

class Classroom():

    def __init__(self, room, capacity): #amenity, priority, building
        self.room = room
        self.status = np.zeros((41,5))
        self.capacity = capacity
#        self.type = type
#        self.amenity = amenity
#        self.building = building
        print(self.status)
#    def set_amenity(self, amenity): self.amenity = amenity
    
#    def set_priority(self, priority): self.priority = priority



    def is_free(self, day, start, finish):
        free = True
        for i in range(start,finish):
            if self.status(day,i) !=0:
                free = False
        return free

    def set_busy(self, day, start, finish):
        if self.is_free(self,start,finish)==True:
            for i in range(start, finish):
                self.status[day, i]=1
            return True
        return False

    def set_course_1h30x2(self, day, start):
        flag = self.is_free(self, day, start, start+5) and self.is_free(self, day+2, start, start+5)
        if flag==True:
            for i in range(start,start+5):
                self.status[day, i]=1
        return flag
    
    def set_course_3h(self, day, start):
        flag = self.is_free(self, day, start, start+11)
        if flag == True:
            for i in range(start, start+11):
                self.status[day, i]=1
        return flag



class Course:
    def __init__(self, name, max_number_of_student): #instructor + credit + amenity + department
        self.name = name
        #self.numer = number
        #self.department = department
        #self.level = level
        self.max_number_of_student = max_number_of_student

    
    def get_name(self): return self.name

    #def get_department(self): return self.department

    #def get_level(self): return self.level

    #def get_instructor(self): return self.instructor

    def get_max_number_of_student(self): return self.max_number_of_student


class Department:
    def __init__(self, department, course):
        self.department = department
        self.course = course
    
    def get_department(self): return self.department

    def get_course(self): return self.course

class Instructor:
    def __init__(self, id, name): 
        self.id = id
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


room_list = [
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
mydict = {}
for i in room_list:
    pass

    