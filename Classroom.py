import numpy as np
List = ['Classroom 1','Classroom 2']
class Classroom():
    DaysOfTheWeekEncoded = { 0:'Monday', 1:'Tuesday', 2:'Wednesday', 3:'Thursday', 4:'Friday'}

    def __init__(self, room, type):
        self.room = room
        self.status = np.array([np.zeros(5)]*6)
        self.type = type
    
    def check_if_free(self, day, time):
        return True if self.status[day,time]==0 else False
    
    def book_a_time(self, day, time):
        if self.check_if_free(day,time)==True:
            self.status[day,time]=1
            return True
        return False


