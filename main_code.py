from Classroom import Classroom
from Course import Course
from Schedule import Schedule
from sample_input import *


schedule = Schedule()

for course in courses:
    schedule.add_course(course)


for i in range(5):
    for j in range(5):
        schedule.table[i][j] = sorted(schedule.table[i][j], key = lambda x : x.capacity)

final_result = [] #list of assigned courses

ok = False
while (not ok):
    min_i, min_j = schedule.find_course_min_indices()
    if (min_i == -1 and min_j == -1):
        ok = True
        break

    course = schedule.table[min_i][min_j][0]

    for classroom in classrooms:
        if (classroom.status[min_i][min_j] == 0 and classroom.capacity >= course.capacity):

            #assign course and classroom
            classroom.status[min_i][min_j] = course
            course.room = classroom
            course.slot = (min_i, min_j)
            final_result.append(course)
        
            #mark course as processed and remove from distribution
            schedule.remove_course(course)

            break

#for course in final_result:
  #  print(f"{course.name}: {course.room.name}, {course.slot}")

for classroom in classrooms:
    print(f"{classroom.name}:")
    for i in range(5):
        for j in range(5):
            if (classroom.status[i][j] != 0):
                print(f"Day {i}, Time slot {j}: Course {classroom.status[i][j].name}")



    
