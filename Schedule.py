class Schedule():
    table = [[[] for _ in range(5)] for _ in range(5)] 
    distribution = [[0 for j in range(5)] for i in range(5)]

    def add_course(self, course):
        for day, time in course.time_slots:
            self.table[day][time].append(course)
            self.distribution[day][time] += 1

    def find_course_min_indices(self):
        min_value = 9999
        min_i, min_j = (-1, -1)

        for i in range(5):
            for j in range(5):
                if (self.distribution[i][j] > 0 and self.distribution[i][j] < min_value):
                    min_value = self.distribution[i][j]
                    min_i, min_j = i, j

        return min_i, min_j

    def remove_course(self, course):
        for day, time in course.time_slots:
            for tmp in self.table[day][time]:
                if (tmp.name == course.name):
                    self.table[day][time].remove(tmp)
                    self.distribution[day][time] -= 1