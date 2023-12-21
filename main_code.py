from Classroom import Classroom
from Course import Course
from sample_input import *

schedule = [[[] for _ in range(5)] for _ in range(5)] 

for course in courses:
    for day, time in course.time_slots:
        schedule[day][time].append(course)

for i in range(5):
    s = "Day " + str(i) + ": "
    for j in range(5):
        s += " " + str(len(schedule[i][j]))
    print(s)

