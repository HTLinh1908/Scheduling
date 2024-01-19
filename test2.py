

class Classroom():
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.status = [["" for _ in range(5)] for _ in range(5)] 
        #print(self.status)

class Course():
    room = ""
    slot = (-1, -1)
    def __init__(self, name, time_slots, capacity):
        self.name = name 
        #the course code, E.g. CS302, MATH101

        self.time_slots = time_slots 
        # 3 possible time slots, each is a tuple (day, starting time), 
        # assumed that each course is 1h30m long

        self.capacity = capacity
    
def main():
    classrooms = [
    #Classroom("CR501", 70),
    Classroom("CR502", 65),
    Classroom("CR1", 55),
    Classroom("CR2", 25),
    Classroom("CR4", 45),
    #Classroom("CR3", 30),
    Classroom("CR5", 15),
    Classroom("CR6", 35),
    Classroom("CR7", 35),
    Classroom("CR8", 45),
    ]
    classrooms = sorted(classrooms, key = lambda x : x.capacity) 
    #increasing capacity order

    course_list = [
        Course("101", [(1, 1), (3, 2)], 50), 
        Course("102", [(1, 4), (2, 0)], 30), 
        Course("103", [(2, 4), (1, 0)], 40), 
        Course("104", [(3, 0), (2, 2)], 50), 
        Course("105", [(3, 2), (2, 2)], 40), 
        Course("106", [(0, 4), (4, 2)], 50), 
        Course("107", [(0, 3), (3, 1)], 10), 
        Course("108", [(0, 0), (4, 4)], 30), 
        Course("109", [(4, 2), (3, 4)], 30), 
        Course("110", [(3, 4), (2, 3)], 30), 
        Course("111", [(3, 4), (2, 3)], 10), 
        Course("112", [(2, 1), (4, 1)], 30), 
        Course("113", [(2, 0), (4, 3)], 30), 
        Course("114", [(2, 3), (1, 4)], 40), 
        Course("115", [(1, 0), (3, 4)], 10), 
        Course("116", [(3, 2), (1, 1)], 10), 
        Course("117", [(4, 3), (0, 4)], 30), 
        Course("118", [(4, 1), (1, 4)], 10), 
        Course("119", [(1, 0), (1, 1)], 10), 
        Course("120", [(3, 0), (1, 0)], 40), 
    ]
    course_list = sorted(course_list, key = lambda x : x.time_slots)
    
    
    def solve(classrooms, course_list):
        for i in course_list:
            for j in classrooms:
                find = find_empty_room(i.time_slots,j.status)
                if not find:
                    return True
                else:
                    day, time = find

                for course in course_list:    
                    for room in classrooms:
                    
                        room.status[day][time] = course.name

                        if solve(classrooms, course_list):
                            return True

                        room.status[day][time]=""
                
        return False

    def valid(classroom, course_name, time_slot):
        pass

    def find_empty_room(prefer_time, classroom):
        for day,time in prefer_time:
            for room in classroom:
                if room[day][time] == "":
                    return day, time
        return None

    for classroom in classrooms:
        print(f"{classroom.name}:")
        for i in range(5):
            for j in range(5):
                if (classroom.status[i][j] != ""):
                    print(f"Day {i}, Time slot {j}: Course {classroom.status[i][j].name}")
    solve(classrooms, course_list)



    

main()