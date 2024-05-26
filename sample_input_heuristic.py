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
classrooms = sorted(classrooms, key=lambda x: x.capacity)
# increasing capacity order

courses = [
    Course("MATH101", "MATH", 100, 0, 0, 50, [[(0, 8, 1.5), (2, 8, 1.5), (4, 8, 1.5)]],),
]
