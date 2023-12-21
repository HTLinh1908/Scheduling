import numpy as np

class Classroom():
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.status = np.array([np.zeros(5)]*5)

