import numpy as np
List = ['Classroom 1','Classroom 2']
class Classroom():
    DaysOfTheWeekEncoded = { 0:'Monday', 1:'Tuesday', 2:'Wednesday', 3:'Thursday', 4:'Friday'}

    def __init__(self, room, capacity, amenity, priority, building):
        self.room = room
        self.status_encoded = np.array([np.zeros(5)]*23)
        self.type = type
        self.status = [[''] * 6] * 23
    
    def set_status(self):
        for i in range(6):
            self.status[1,i]=DaysOfTheWeekEncoded.get(i)

    def is_free(self, day, start, finish):
        free = True
        for index in range(start,finish):
            if self.status_encoded(day,index) ==1:
                free = False
        return free

        return True if self.status_encoded[day,time]==0 else False
    
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

C = Classroom('abc',1)

print(C.status_encoded)