from Course import Course
from Classroom import Classroom

classrooms = [
    Classroom("CR501", 70),
    Classroom("CR502", 65),
    Classroom("CR1", 55),
    Classroom("CR2", 25),
    Classroom("CR4", 45),
    Classroom("CR3", 30),
    Classroom("CR5", 15),
    Classroom("CR6", 35),
    Classroom("CR7", 35),
    Classroom("CR8", 45),
]
classrooms = sorted(classrooms, key = lambda x : x.capacity) 
#increasing capacity order

courses = [
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