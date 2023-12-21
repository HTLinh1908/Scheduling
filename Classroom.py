import numpy as np
List = ['Classroom 1','Classroom 2']

class Classroom():
    def __init__(self, room, type):
        self.room = room
        self.status = np.array([np.zeros(5)]*6)
        self.type = type
lmouse = Classroom('Classroom 1')

print(lmouse.status)
