class Classroom:
    def __init__(self, name, capacity, id):
        self.name = name
        self.capacity = capacity
        self.id = id

    def get_capacity(self):
        return self.capacity

    def __str__(self):
        return self.name