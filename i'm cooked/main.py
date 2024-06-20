import time

from Setting import *

start = time.time()

timeslot_priority_list = [1, 2, 3, 4, 0, 5]
list_of_courses = sorted(input_courses, key=lambda course: (course.level, course.course_length, -course.capacity))


def assign_course(course_list, available_classrooms):
    while len(course_list) != 0:
        course = course_list.pop(0)

        for classroom in available_classrooms:
            if course.get_capacity() >= classroom.get_capacity():
                continue

            match course.course_length:
                case 0:
                    for start_time in timeslot_priority_list:
                        chosen = False
                        for day in range(2):
                            classroom_status = classroom.get_status()
                            if classroom_status[day][start_time] == "":
                                classroom.set_status(day, start_time, course.get_name())
                                classroom.set_status(day + 2, start_time, course.get_name())
                                chosen = True
                                break

                case 1:
                    pass


assign_course(list_of_courses, classrooms)

print("--- %s seconds ---" % (time.time() - start))