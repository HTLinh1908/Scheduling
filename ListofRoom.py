import numpy as np
List = ['CR1','CR2']
class Classroom():
    def __init__(self, room, type):
        self.room = room
        self.status = np.array([np.zeros(5)]*6)
        self.type = type
lmouse = Classroom('CR1')

print(lmouse.status)
