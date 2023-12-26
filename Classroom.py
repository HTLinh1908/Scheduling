import numpy as np

class Classroom():
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.status = [[0 for _ in range(5)] for _ in range(5)] 
        print(self.status)

