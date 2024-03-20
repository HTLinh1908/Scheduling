class Classroom:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.availability = [[0 for _ in range(5)] for _ in range(5)]

    def get_capacity(self):
        return self.capacity