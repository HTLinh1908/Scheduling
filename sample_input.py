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
    Course("101", [(0, 3), (1, 2)], 10), 
    Course("102", [(1, 0), (2, 1)], 10), 
    Course("103", [(2, 4), (1, 4)], 40), 
    Course("104", [(0, 4), (1, 4)], 50), 
    Course("105", [(1, 3), (1, 4)], 20), 
    Course("106", [(1, 2), (0, 0)], 10), 
    Course("107", [(2, 3), (1, 1)], 40), 
    Course("108", [(0, 4), (0, 0)], 40), 
    #Course("109", [(0, 0), (0, 4)], 10), 
    Course("110", [(0, 4), (0, 1)], 30), 
    Course("111", [(2, 1), (2, 3)], 30), 
    Course("112", [(1, 0), (1, 3)], 10), 
    Course("113", [(1, 2), (1, 4)], 40), 
    #Course("114", [(0, 4), (1, 2)], 10), 
    Course("115", [(1, 4), (0, 2)], 10), 
    Course("116", [(0, 1), (1, 2)], 10), 
    Course("117", [(0, 3), (2, 0)], 50), 
    Course("118", [(0, 2), (1, 4)], 10), 
    Course("119", [(0, 4), (2, 2)], 40), 
    Course("120", [(2, 1), (0, 0)], 10), 
    Course("121", [(0, 3), (1, 0)], 30), 
    Course("122", [(1, 1), (0, 1)], 10), 
    Course("123", [(0, 0), (0, 3)], 50), 
    Course("124", [(2, 3), (2, 2)], 10), 
    Course("125", [(2, 3), (2, 4)], 40), 
    #Course("126", [(0, 2), (0, 4)], 10), 
    Course("127", [(0, 1), (1, 0)], 30), 
    Course("128", [(2, 2), (1, 0)], 40), 
    Course("129", [(0, 1), (0, 2)], 20), 
    Course("130", [(1, 1), (0, 3)], 50), 
    Course("131", [(1, 4), (2, 1)], 50), 
    Course("132", [(1, 3), (1, 1)], 50), 
    Course("133", [(0, 4), (2, 4)], 10), 
    Course("134", [(2, 1), (2, 2)], 20), 
    Course("135", [(1, 2), (2, 1)], 30), 
    Course("136", [(2, 2), (0, 0)], 40), 
    Course("137", [(1, 4), (0, 0)], 40), 
    Course("138", [(0, 1), (2, 1)], 30), 
    Course("139", [(1, 4), (0, 4)], 30), 
    Course("140", [(1, 2), (0, 2)], 40), 
    Course("141", [(1, 2), (2, 3)], 20), 
    Course("142", [(1, 4), (1, 3)], 50), 
    Course("143", [(1, 2), (0, 4)], 40), 
    Course("144", [(2, 3), (2, 2)], 10), 
    Course("145", [(0, 2), (0, 1)], 10), 
    Course("146", [(0, 2), (1, 2)], 30), 
    Course("147", [(2, 1), (0, 3)], 50), 
    Course("148", [(1, 0), (1, 1)], 20), 
    Course("149", [(1, 2), (1, 3)], 40), 
    Course("150", [(2, 2), (2, 3)], 20), 

]

