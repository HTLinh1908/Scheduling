from Classroom import Classroom
from Course import Course
from Schedule import Schedule
from sample_input import *


schedule = Schedule()

for course in courses:
    schedule.add_course(course)


for i in range(5):
    for j in range(5):
        schedule.table[i][j] = sorted(schedule.table[i][j], key = lambda x : x[0].capacity)

final_result = [] #list of assigned courses

ok = False
while (not ok):
    min_i, min_j = schedule.find_course_min_indices()
    if (min_i == -1 and min_j == -1):
        ok = True
        break
    
    course, first_or_second_lesson = schedule.table[min_i][min_j][0]
    #print(f"{course.name} preference {preference} selected")

    for classroom in classrooms:
            if (classroom.status[min_i][min_j] == 0 and classroom.capacity >= course.capacity):

                #assign course and classroom
                if (first_or_second_lesson == 0):
                    classroom.status[min_i][min_j] = course
                    classroom.status[min_i+2][min_j] = course
                    course.slot = (min_i, min_j)
                else:
                    classroom.status[min_i-2][min_j] = course
                    classroom.status[min_i][min_j] = course
                    course.slot = (min_i-2, min_j)

            
                #mark course as processed and remove from distribution
                course.room = classroom
                final_result.append(course)
                #print(f"ok {course.name} {course.room.name} {course.slot}")
                schedule.remove_course(course)
                #print(f"ok {course.name}")
                break


### output value 
with open("sample_output.txt", "w") as output_file:
    for i in range(5):
        for k in range(len(classrooms)):
            classroom = classrooms[k]
            print(classroom.name, end= "row" if (k == len(classrooms) -1 ) else " ", file=output_file)
        for j in range(5):
            for k in range(len(classrooms)):
                classroom = classrooms[k]
                if classroom.status[i][j] != 0:
                    print(classroom.status[i][j].name, end = "row" if (k == len(classrooms) -1 ) else " ", file=output_file)
                else:
                    print("_", end = "row" if (k == len(classrooms) -1 ) else " ", file=output_file)
        print("end", file=output_file)


    
