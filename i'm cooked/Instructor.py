class Instructor:
    def __init__(self, name):
        self.name = name
        self.busy_slots = []

    def __str__(self):
        return self.name

    def get_name(self):
        return self.name

    def get_busy_slots(self):
        return self.busy_slots

    def set_busy_slots(self, day, time):
        if (day, time) not in self.busy_slots:
            self.busy_slots += [(day, time)]
            return True
        return False

