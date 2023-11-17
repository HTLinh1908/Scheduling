import numpy as np
List = ['Classroom 1','Classroom 2']
class Classroom():
    DaysOfTheWeekEncoded = { 0:'Monday', 1:'Tuesday', 2:'Wednesday', 3:'Thursday', 4:'Friday'}

    def __init__(self, room, type):
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
        if self.check_if_free(day,time)==True:
            self.status_encoded[day,time]=1
            return True
        return False


C = Classroom('abc',1)

print(C.status_encoded)