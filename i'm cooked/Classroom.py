
class Classroom:
    def __init__(self, name, capacity):
        self.name = name  # type: str # name of the classroom
        self.capacity = capacity  # type: int # capacity of the classroom
        self.status = [["" for i in range(6)] for i in range(5)] # status of the classroom

    def __str__(self):
        return self.name

    def get_capacity(self):
        return self.capacity

    def get_status(self):
        return self.status

    def set_status(self, day, time, course_name):
        self.status[day][time] = course_name


