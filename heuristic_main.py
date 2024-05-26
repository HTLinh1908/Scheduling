from sample_input_heuristic import *

levels = [[], [], [], []]
timeslot_priority_list = [0, 1, 2, 3, 4, 5]
# 9:45, 11:15, 13:15, 15h, 8h, 16:45

res = [[["" for _ in range(len(classrooms))] for _ in range(6)] for _ in range(5)]

courses = sorted(courses, key=lambda x: (x.level, x.type, -x.capacity))

for course in courses:
    for j in range(len(classrooms)):
        if course.capacity <= classrooms[j].capacity:
            if course.type == 0:  # type 0: 1.5h
                for k in timeslot_priority_list:
                    if course.chosen_slot != (-1, -1, -1):
                        continue
                    if res[0][k][j] == "" and res[2][k][j] == "":
                        res[0][k][j] = course.name
                        res[2][k][j] = course.name
                        course.chosen_slot = [(0, k, j), (2, k, j)]
                        break
                    if res[1][k][j] == "" and res[3][k][j] == "":
                        res[1][k][j] = course.name
                        res[3][k][j] = course.name
                        course.chosen_slot = [(1, k, j), (3, k, j)]
                        break
            else:  # type 1: 3h
                for k in range(len(timeslot_priority_list) - 1):  # latest 3h course can just be 15:00
                    for day in range(4, -1, -1):
                        if course.chosen_slot != (-1, -1, -1):
                            continue
                        if res[day][k][j] == "" and res[day][k+1][j] == "":
                            res[day][k][j] = course.name
                            res[day][k+1][j] = course.name
                            course.chosen_slot = (day, k, j)
                            break

"""OUTPUT"""
time_in_day = ["8AM", "9:45AM", "11:30AM", "1:15PM", "3PM", "4:45PM"]

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