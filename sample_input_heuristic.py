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
    # Fall 2023

    # Applied Maths
    Course("MATH101", "MATH", 100, 0, 0, 50),
    Course("MATH102", "MATH", 100, 0, 0, 50),
    Course("MATH103", "MATH", 100, 0, 0, 50),
    Course("MATH105", "MATH", 100, 0, 0, 50),
    Course("MATH105", "MATH", 100, 0, 0, 50),
    Course("MATH205", "MATH", 200, 0, 0, 40),
    Course("MATH301", "MATH", 300, 0, 0, 30),

    # Arts and Media Studies
    Course("ARTS101", "ARTS", 100, 0, 0, 50),
    Course("ARTS103", "ARTS", 100, 0, 0, 50),
    Course("ARTS104", "ARTS", 100, 0, 0, 25),
    Course("ARTS108", "ARTS", 100, 0, 0, 25),
    Course("ARTS112", "ARTS", 100, 1, 0, 25),
    Course("ARTS204", "ARTS", 200, 0, 0, 25),
    Course("ARTS210", "ARTS", 200, 1, 0, 30),
    Course("ARTS301", "ARTS", 300, 1, 0, 30),
    Course("ARTS307", "ARTS", 300, 1, 0, 30),

    # Computer Science
    Course("CS101", "CS", 100, 0, 0, 50),
    Course("CS103", "CS", 100, 0, 0, 50),
    Course("CS104", "CS", 100, 0, 0, 50),
    Course("CS203", "CS", 200, 0, 0, 30),
    Course("CS207", "CS", 200, 1, 0, 40),
    Course("CS210", "CS", 200, 0, 0, 40),
    Course("CS302", "CS", 300, 0, 0, 30),
    Course("CS304", "CS", 300, 0, 0, 40),
    Course("CS309", "CS", 300, 1, 0, 40),

    # Economics
    Course("ECON101", "ECON", 100, 0, 0, 50),
    Course("ECON101", "ECON", 100, 0, 0, 40),
    Course("ECON102", "ECON", 100, 0, 0, 50),
    Course("ECON103", "ECON", 100, 0, 0, 50),
    Course("ECON103", "ECON", 100, 0, 0, 40),
    Course("ECON205", "ECON", 200, 1, 0, 50),
    Course("ECON209", "ECON", 200, 0, 0, 40),
    Course("ECON305", "ECON", 300, 0, 0, 35),
    Course("ECON311", "ECON", 300, 1, 0, 30),

    # Engineer
    Course("ENG102", "ENG", 100, 0, 0, 30),
    Course("ENG201", "ENG", 200, 0, 0, 40),
    Course("ENG202", "ENG", 200, 0, 0, 30),
    Course("ENG210", "ENG", 200, 0, 0, 40),
    Course("ENG308", "ENG", 300, 0, 0, 25),

    # History
    Course("HIS103", "HIS", 100, 0, 0, 50),
    Course("HIS150", "HIS", 100, 0, 0, 50),
    Course("HIS212", "HIS", 200, 0, 0, 40),
    Course("HIS213", "HIS", 200, 0, 0, 40),
    Course("HIS302", "HIS", 300, 0, 0, 30),
    Course("HIS308", "HIS", 300, 1, 0, 30),

    # Integrated Science
    Course("IS105", "IS", 100, 0, 0, 50),
    Course("IS211", "IS", 200, 0, 0, 25),
    Course("IS213", "IS", 200, 1, 0, 25),
    Course("IS305", "IS", 300, 0, 0, 15),
    Course("IS306", "IS", 300, 0, 0, 15),

    # Literature
    Course("LIT102", "LIT", 100, 0, 0, 50),
    Course("LIT207", "LIT", 200, 0, 0, 40),
    Course("LIT208", "LIT", 200, 0, 0, 40),
    Course("LIT310", "LIT",300, 0, 0, 30),
    Course("LIT311", "LIT",300, 0, 0, 30),

    # Music
    Course("MUSC201", "MUSC", 200, 0, 0, 40),

    # Psychology
    Course("PSY101", "PSY", 100, 0, 0, 50),
    Course("PSY202", "PSY", 200, 0, 0, 40),
    Course("PSY204", "PSY",200, 1, 0, 40),
    Course("PSY205", "PSY", 200, 0, 0, 40),
    Course("PSY209", "PSY", 200, 0, 0, 40),
    Course("PSY308", "PSY", 300, 1, 0, 20),

    # Social Studies
    Course("SOCI102", "SOCI", 100, 0, 0, 70),  # What the fuck is this course? Originally this course capacity is 80
    Course("SOCI105", "SOCI",100, 0, 0, 50),
    Course("SOCI109", "SOCI",100, 0, 0, 50),
    Course("SOCI211", "SOCI",200,0,0,40),
    Course("SOCI219","SOCI",200, 0, 0, 40),

    # Vietnam Studies
    Course("VS106", "VS", 100, 1, 0, 50),
    Course("VS208", "VS", 200, 0, 0, 40),
    Course("VS213", "VS", 200, 0, 0, 40),
    Course("VS214", "VS", 200, 1, 0, 20),
    Course("VS305", "VS", 300, 1, 0, 30),
    Course("VS306", "VS", 300, 0, 0, 30),

    # Global Humanities and Social Changes
    Course("CORE101", "CORE", 100, 0, 0, 18),
    Course("CORE101", "CORE", 100, 0, 0, 18),
    Course("CORE101", "CORE", 100, 0, 0, 18),
    Course("CORE101", "CORE", 100, 0, 0, 18),
    Course("CORE101", "CORE", 100, 0, 0, 18),
    Course("CORE101", "CORE", 100, 0, 0, 18),
    Course("CORE101", "CORE", 100, 0, 0, 18),
    Course("CORE101", "CORE", 100, 0, 0, 18),
    Course("CORE101", "CORE", 100, 0, 0, 18),
    Course("CORE101", "CORE", 100, 0, 0, 18),

    # Quantitative Reasoning for a Digital Age
    Course("CORE103", "CORE", 100, 0, 0, 30),
    Course("CORE103", "CORE", 100, 0, 0, 30),
    Course("CORE103", "CORE", 100, 0, 0, 30),
    Course("CORE103", "CORE", 100, 0, 0, 30),

    # Scientific Enquiry
    Course("CORE104", "CORE", 100, 0, 0, 30),
    Course("CORE104", "CORE", 100, 0, 0, 30),
    Course("CORE104", "CORE", 100, 0, 0, 30),
    Course("CORE104", "CORE", 100, 0, 0, 30),
    Course("CORE104", "CORE", 100, 0, 0, 30),

    # Design and System Thinking
    Course("CORE105", "CORE", 100, 0, 0, 25),
    Course("CORE105", "CORE", 100, 0, 0, 25),
    Course("CORE105", "CORE", 100, 0, 0, 25),
    Course("CORE105", "CORE", 100, 0, 0, 25),
]
