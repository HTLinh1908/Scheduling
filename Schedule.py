from Classroom import Classroom

class Schedule():
    table = [[[] for _ in range(5)] for _ in range(5)] 
    distribution = [[0 for j in range(5)] for i in range(5)]

    def add_course(self, course):
        for i in range(len(course.time_slots)):
            day, time = course.time_slots[i]
            self.table[day][time].append((course, 0))
            self.distribution[day][time] += 1

            self.table[day+2][time].append((course, 1))
            self.distribution[day+2][time] += 1
            
    def remove_course(self, course):
        for day, time in course.time_slots:
            for tmp in self.table[day][time]:
                if (tmp[0].name == course.name):
                    # print(f"{tmp[2]} {course.preference}")
                    # print(f"removed {day} {time}")
                    # print(f"{self.table[day][time][0][0].name} dmmm")
                    self.table[day][time].remove(tmp)
                    self.table[day+2][time].remove((tmp[0],1))
                    # if (len(self.table[day][time])>0):
                    #     print(f"{self.table[day][time][0][0].name} hihii")
                    self.distribution[day][time] -= 1
                    self.distribution[day+2][time] -= 1
                    # print("done")

    def find_course_min_indices(self):
        min_value = 9999
        min_i, min_j = (-1, -1)

        for i in range(5):
            for j in range(5):
                if (self.distribution[i][j] > 0 and self.distribution[i][j] < min_value):
                    min_value = self.distribution[i][j]
                    min_i, min_j = i, j
        return min_i, min_j
    
        
