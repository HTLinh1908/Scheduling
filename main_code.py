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

#for course in final_result:
  #  print(f"{course.name}: {course.room.name}, {course.slot}")

# for classroom in classrooms:
#     print(f"{classroom.name}:")
#     for i in range(5):
#         for j in range(5):
#             if (classroom.status[i][j] != 0):
#                 print(f"Day {i}, Time slot {j}: Course {classroom.status[i][j].name}")
#classrooms = sorted(classrooms, key = lambda x : x.name) 
with open("sample_output.txt", "w") as output_file:
    # for classroom in classrooms:
    #     print(classroom.name, end=" ", file=output_file)
    # print(file=output_file)
    days=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    for i in range(5):
        print(days[i], file=output_file)
        for classroom in classrooms:
            print(classroom.name, end=" ", file=output_file)
        print(file=output_file)
        for j in range(5):
            for classroom in classrooms:
                if classroom.status[i][j] != 0:
                    print(classroom.status[i][j].name, end=" ", file=output_file)
                else:
                    print("_", end=" ", file=output_file)
            print(file=output_file)
        print(file=output_file)


    
