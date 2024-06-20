from Course import Course
from Classroom import Classroom
from Instructor import Instructor

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
    Classroom("Makerspace", 40),
    Classroom("Ideation_Hub", 30)
]
classrooms = sorted(classrooms, key=lambda x: x.capacity)
# increasing capacity order

van_phung_truong_son = Instructor("Van Phung Truong Son")
le_nhat_tan = Instructor("Le Nhat Tan")
nguyen_trung_hieu = Instructor("Nguyen Trung Hieu")
tran_vinh_linh = Instructor("Tran Vinh Linh")

input_courses = [
    # Spring 2024

    # Applied Maths
    Course("MATH104", "Multivariable Calculus", "MATH", 100, 0, 50, [van_phung_truong_son], 0),
    Course("MATH201", "Differential Equation", "MATH", 200, 0, 40, [nguyen_trung_hieu], 0),
    Course("MATH202", "Discrete Mathematics", "MATH", 200, 1, 40, [tran_vinh_linh], 0),
    Course("MATH306", "Financial Mathematics", "MATH", 300, 1, 30, [le_nhat_tan], 0),
    Course("MATH307", "Real Analysis", "MATH", 300, 0, 30, [nguyen_trung_hieu], 0),
    Course("MATH310", "Mathematical Statistics", "MATH", 300, 0, 30, [van_phung_truong_son], 0),
    Course("MATH311", "Mathematics Research Seminar", "MATH", 300, 1, 30, [tran_vinh_linh, van_phung_truong_son, nguyen_trung_hieu, le_nhat_tan], 0),

    # Engineer
    Course("ENG104", "Sensors, Measurement and Analysis", "ENG", 100, 0, 30, "Nguyen Hop Minh", 0),
    Course("ENG207", "Mechanical Design", "ENG", 200, 0, 30, "Doan Nhat Minh", 0),
    Course("ENG208", "Electronics Device and Circuits", "ENG", 200, 0, 30, "Quan Le", 0),
    Course("ENG209", "Signals, Systems and Control", "ENG", 200, 0, 30, "Truong Trung Kien", 0),
    Course("ENG301", "Computer Vision" , "ENG", 300, 0, 30, "Phung Manh Duong", 0),
    Course("ENG309", "Industrial Design", "ENG", 300, 0, 30, "Quan Le", 0),
    Course("ENG310", "Performance Evaluation In Built Environment", "ENG", 300, 0, 30, "Nguyen Hop Minh", 0),


    # Modern Vietnamese Culture and Society
    Course("CORE102", "Modern Vietnamese Culture and Society", "CORE", 100, 0, 30, "Luong Ngoc Tram", 0),
    Course("CORE102", "Modern Vietnamese Culture and Society", "CORE", 100, 0, 30, "Nguyen Thi Lan", 0),
    Course("CORE102", "Modern Vietnamese Culture and Society", "CORE", 100, 0, 30, "Vu Ngoc Bao Yen", 0),
    Course("CORE102", "Modern Vietnamese Culture and Society", "CORE", 100, 0, 30, "Pamela Corey", 0),
    Course("CORE102", "Modern Vietnamese Culture and Society", "CORE", 100, 0, 30, "Nicolas Weber", 0),
    Course("CORE102", "Modern Vietnamese Culture and Society", "CORE", 100, 0, 30, "Nguyen Thanh Trung", 0),

    # Quantitative Reasoning for a Digital Age
    Course("CORE103", "Quantitative Reasoning for a Digital Age", "CORE", 100, 0, 30, "Phan Tuan Ngoc", 0),
    Course("CORE103", "Quantitative Reasoning for a Digital Age", "CORE", 100, 0, 30, "Le Nhat Tan", 0),
    Course("CORE103", "Quantitative Reasoning for a Digital Age", "CORE", 100, 0, 30, "Phan Thanh Trung", 0),
    Course("CORE103", "Quantitative Reasoning for a Digital Age", "CORE", 100, 0, 30, "Janny W. Fritzen", 0),

    # Scientific Enquiry
    Course("CORE104", "Scientific Enquiry", "CORE", 100, 0, 30, "Jesse Hollister", 0),
    Course("CORE104", "Scientific Enquiry", "CORE", 100, 0, 30, "Hoang Minh To Nga", 0),
    Course("CORE104", "Scientific Enquiry", "CORE", 100, 0, 30, "Gareth Davey", 0),
    Course("CORE104", "Scientific Enquiry", "CORE", 100, 0, 30, "Nguyen Thi Hong Dung", 0),

    # Design and System Thinking
    Course("CORE105", "Design and System Thinking", "CORE", 100, 0, 30, "Truong Trung Kien", 0),
    Course("CORE105", "Design and System Thinking", "CORE", 100, 0, 30, "Phung Manh Duong", 0),
    Course("CORE105", "Design and System Thinking", "CORE", 100, 0, 30, "Doan Nhat Minh", 0),
    Course("CORE105", "Design and System Thinking", "CORE", 100, 0, 30, "Nguyen Hop Minh", 0),
]
