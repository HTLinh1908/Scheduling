import time

from sample_input_heuristic import *

start = time.time()

levels = [[], [], [], []]
timeslot_priority_list = [0, 1, 2, 3, 4, 5]
# 9:45, 11:15, 13:15, 15h, 8h, 16:45

res = [[["" for _ in range(len(classrooms))] for _ in range(6)] for _ in range(5)]

#engineering and DST courses
technical_courses = [course for course in courses if course.major == "ENG" or course.name == "CORE105"]
technical_courses = sorted(technical_courses, key=lambda x: (x.level, x.type, -x.capacity))
technical_classrooms = [classroom for classroom in classrooms
                        if classroom.name == "Makerspace"]
technical_classrooms = sorted(technical_classrooms, key=lambda x: x.capacity)

#other courses
courses = [course for course in courses if course.major != "ENG" and course.name != "CORE105"]
courses = sorted(courses, key=lambda x: (x.level, x.type, -x.capacity))
non_technical_classrooms = [classroom for classroom in classrooms
                            if classroom.name != "Makerspace"]
non_technical_classrooms = sorted(non_technical_classrooms, key=lambda x: x.capacity)


def assign_course(courses, available_classrooms):
    for course in courses:
        for j in range(len(available_classrooms)):
            if course.capacity <= available_classrooms[j].capacity:
                if course.type == 0:  # type 0: 1.5h
                    for k in timeslot_priority_list:
                        if course.chosen_slot != (-1, -1, -1):
                            continue
                        if res[0][k][available_classrooms[j].id] == "" and res[2][k][available_classrooms[j].id] == "":
                            res[0][k][available_classrooms[j].id] = course.name
                            res[2][k][available_classrooms[j].id] = course.name
                            course.chosen_slot = [(0, k, available_classrooms[j].id), (2, k, available_classrooms[j].id)]
                            break
                        if res[1][k][available_classrooms[j].id] == "" and res[3][k][j] == "":
                            res[1][k][available_classrooms[j].id] = course.name
                            res[3][k][available_classrooms[j].id] = course.name
                            course.chosen_slot = [(1, k, available_classrooms[j].id), (3, k, available_classrooms[j].id)]
                            break
                else:  # type 1: 3h
                    for k in range(len(timeslot_priority_list) - 1):  # latest 3h course can just be 15:00
                        for day in range(4, -1, -1):
                            if course.chosen_slot != (-1, -1, -1):
                                continue
                            if res[day][k][available_classrooms[j].id] == "" and res[day][k+1][available_classrooms[j].id] == "":
                                res[day][k][available_classrooms[j].id] = course.name
                                res[day][k+1][available_classrooms[j].id] = course.name
                                course.chosen_slot = (day, k, available_classrooms[j].id)
                                break


assign_course(technical_courses, technical_classrooms)
assign_course(courses, non_technical_classrooms)
"""OUTPUT"""
time_in_day = ["8AM", "9:45AM", "11:30AM", "1:15PM", "3PM", "4:45PM"]

classrooms = sorted(classrooms, key=lambda x: x.id)
with open("output.txt", "w") as f:
    for day in range(5):
        f.write(" ")
        for i in range(len(classrooms)):
            f.write(classrooms[i].name + ("row" if i == len(classrooms) - 1 else " "))
        for i in range(6):
            f.write(time_in_day[i] + " ")
            for j in range(len(classrooms)):
                f.write((res[day][i][j] if res[day][i][j] != "" else "_")
                        + ("row" if j == len(classrooms) - 1 else " "))
        f.write("end\n")

success_count = 0
for course in courses:
    if course.chosen_slot != (-1, -1, -1):
        success_count += 1
    else:
        print(f"Failed to assign {course.name}: capacity {course.capacity}, type {course.type}")

print(f"Success rate: {success_count}/{len(courses)}")
print("--- %s seconds ---" % (time.time() - start))