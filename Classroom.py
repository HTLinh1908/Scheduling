import numpy as np
import random

class Classroom():

    def __init__(self, room, capacity): #amenity, priority, building
        self.room = room
        self.capacity = capacity
        self.status = np.zeros((41,5))
        
 
#        self.type = type
#        self.amenity = amenity
#        self.building = building
#    def set_amenity(self, amenity): self.amenity = amenity
    
#    def set_priority(self, priority): self.priority = priority

class Course:
    room = ""
    slot =(-1,-1)
    def __init__(self, name, prefered_day_time, max_number_of_student): #frequency, instructor + credit + amenity + department
        self.name = name
        #self.numer = number
        #self.department = department
        #self.level = level
        self.max_number_of_student = max_number_of_student
        #self.frequency = frequency
        #list of numbers
        #1 is 2 times a week 1h30m each
        #2 is 1 time a week for 3h once
        #3 is 2 times a week for 3h each
        self.prefered_day_time = prefered_day_time
        # Array of list indluding numbers (x, y) representing (day, time)
        # x
        # 0: Monday 
        # 1: Tuesday
        # 2: Wednesday
        # 3: Thursday
        # 4: Friday
        # y
        # 0: 8:00 am start
        # 1: 9:45am start
        # 2: 11:30 am start
        # 3: 1:15 pm start
        # 4: 3:00 pm start
        # 5: 4h45 pm start
    def get_name(self): return self.name

    #def get_department(self): return self.department

    #def get_level(self): return self.level

    #def get_instructor(self): return self.instructor

    def get_max_number_of_student(self): return self.max_number_of_student


#class Department:
#    def __init__(self, department, course):
#       self.department = department
#        self.course = course
    
#    def get_department(self): return self.department

#    def get_course(self): return self.course

#class Instructor:
#    def __init__(self, id, name): 
#        self.id = id
#        self.name = name
#    def get_id(self): return self.id
#    def get_name(self): return self.name

#class Class:
#    def __init__(self, department, course):
#        self.department = department
#        self.course = course
#        self.instructor = None
#        self.room = None
    
#    def get_department(self): return self.department

#    def get_course(self): return self.course

#    def get_instructor(self): return self.instructor
    
#    def get_room(self): return self.room

#    def set_instructor(self, instructor): self.instructor = instructor

#    def set_room(self, room): self.room = room

class Schedule():
    table = [[[] for _ in range(5)] for _ in range(5)] 
    distribution = [[0 for j in range(5)] for i in range(5)]
    
    def is_free(self, day, start, finish):
        free = True
        for i in range(start,finish):
            if self.status(day,i) !=0:
                free = False
        return free

    #def set_course(self, day, start, finish):
    #    if self.is_free(self,start,finish)==True:
    #        for i in range(start, finish):
    #            self.status[day, i]=1
    #        return True
    #    return False

    #def add_course_1h30x2(self, day, start):
    #    flag = self.is_free(self, day, start, start+5) and self.is_free(self, day+2, start, start+5)
    #    if flag==True:
    #        for i in range(start,start+5):
    #            self.status[day, i]=1
    #    return flag
    
    #def add_course_3h(self, day, start):
    #    flag = self.is_free(self, day, start, start+11)
    #    if flag == True:
    #        for i in range(start, start+11):
    #            self.status[day, i]=1
    #    return flag
    def add_course(self, course):
        for day, time in course.prefered_day_time:
            self.table[day][time].append(course)
            self.distribution[day][time] += 1
    def find_course_min_indices(self):
        min_value = 9999
        min_i, min_j = (-1, -1)

        for i in range(5):
            for j in range(5):
                if (self.distribution[i][j] > 0 and self.distribution[i][j] < min_value):
                    min_value = self.distribution[i][j]
                    min_i, min_j = i, j


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

course_list = [
    Course("ECON307", 30),
    Course("HIS310", 30),
    Course("MATH308", 30),
    Course("ECON102", 50),
    Course("MATH105", 50),
    Course("MUSIC102", 50),
    Course("CS204", 40),
    Course("CS311", 30),
    Course("SOCI218",40),
    Course("CS301", 30),
    Course("SOCI217",40)
]





    