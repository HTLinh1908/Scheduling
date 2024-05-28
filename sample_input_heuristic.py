from Course import Course
from Classroom import Classroom

classrooms = [
    Classroom("CR501", 70, 0),
    Classroom("CR502", 65, 1),
    Classroom("CR1", 55, 2),
    Classroom("CR2", 25, 3),
    Classroom("CR4", 45, 4),
    Classroom("CR3", 30, 5),
    Classroom("CR5", 15, 6),
    Classroom("CR6", 35, 7),
    Classroom("CR7", 35, 8),
    Classroom("CR8", 45, 9),
    Classroom("Makerspace", 40, 10),
    Classroom("Ideation_Hub", 30, 11)
]
classrooms = sorted(classrooms, key=lambda x: x.capacity)
# increasing capacity order

# courses = [
#     # Fall 2023
#
#     # Applied Maths
#     Course("MATH101", "MATH", 100, 0, 0, 50),
#     Course("MATH102", "MATH", 100, 0, 0, 50),
#     Course("MATH103", "MATH", 100, 0, 0, 50),
#     Course("MATH105", "MATH", 100, 0, 0, 50),
#     Course("MATH105", "MATH", 100, 0, 0, 50),
#     Course("MATH205", "MATH", 200, 0, 0, 40),
#     Course("MATH301", "MATH", 300, 0, 0, 30),
#
#     # Arts and Media Studies
#     Course("ARTS101", "ARTS", 100, 0, 0, 50),
#     Course("ARTS103", "ARTS", 100, 0, 0, 50),
#     Course("ARTS104", "ARTS", 100, 0, 0, 25),
#     Course("ARTS108", "ARTS", 100, 0, 0, 25),
#     Course("ARTS112", "ARTS", 100, 1, 0, 25),
#     Course("ARTS204", "ARTS", 200, 0, 0, 25),
#     Course("ARTS210", "ARTS", 200, 1, 0, 30),
#     Course("ARTS301", "ARTS", 300, 1, 0, 30),
#     Course("ARTS307", "ARTS", 300, 1, 0, 30),
#
#     # Computer Science
#     Course("CS101", "CS", 100, 0, 0, 50),
#     Course("CS103", "CS", 100, 0, 0, 50),
#     Course("CS104", "CS", 100, 0, 0, 50),
#     Course("CS203", "CS", 200, 0, 0, 30),
#     Course("CS207", "CS", 200, 1, 0, 40),
#     Course("CS210", "CS", 200, 0, 0, 40),
#     Course("CS302", "CS", 300, 0, 0, 30),
#     Course("CS304", "CS", 300, 0, 0, 40),
#     Course("CS309", "CS", 300, 1, 0, 40),
#
#     # Economics
#     Course("ECON101", "ECON", 100, 0, 0, 50),
#     Course("ECON101", "ECON", 100, 0, 0, 40),
#     Course("ECON102", "ECON", 100, 0, 0, 50),
#     Course("ECON103", "ECON", 100, 0, 0, 50),
#     Course("ECON103", "ECON", 100, 0, 0, 40),
#     Course("ECON205", "ECON", 200, 1, 0, 50),
#     Course("ECON209", "ECON", 200, 0, 0, 40),
#     Course("ECON305", "ECON", 300, 0, 0, 35),
#     Course("ECON311", "ECON", 300, 1, 0, 30),
#
#     # Engineer
#     Course("ENG102", "ENG", 100, 0, 0, 30),
#     Course("ENG201", "ENG", 200, 0, 0, 40),
#     Course("ENG202", "ENG", 200, 0, 0, 30),
#     Course("ENG210", "ENG", 200, 0, 0, 40),
#     Course("ENG308", "ENG", 300, 0, 0, 25),
#
#     # History
#     Course("HIS103", "HIS", 100, 0, 0, 50),
#     Course("HIS150", "HIS", 100, 0, 0, 50),
#     Course("HIS212", "HIS", 200, 0, 0, 40),
#     Course("HIS213", "HIS", 200, 0, 0, 40),
#     Course("HIS302", "HIS", 300, 0, 0, 30),
#     Course("HIS308", "HIS", 300, 1, 0, 30),
#
#     # Integrated Science
#     Course("IS105", "IS", 100, 0, 0, 50),
#     Course("IS211", "IS", 200, 0, 0, 25),
#     Course("IS213", "IS", 200, 1, 0, 25),
#     Course("IS305", "IS", 300, 0, 0, 15),
#     Course("IS306", "IS", 300, 0, 0, 15),
#
#     # Literature
#     Course("LIT102", "LIT", 100, 0, 0, 50),
#     Course("LIT207", "LIT", 200, 0, 0, 40),
#     Course("LIT208", "LIT", 200, 0, 0, 40),
#     Course("LIT310", "LIT",300, 0, 0, 30),
#     Course("LIT311", "LIT",300, 0, 0, 30),
#
#     # Music
#     Course("MUSC201", "MUSC", 200, 0, 0, 40),
#
#     # Psychology
#     Course("PSY101", "PSY", 100, 0, 0, 50),
#     Course("PSY202", "PSY", 200, 0, 0, 40),
#     Course("PSY204", "PSY",200, 1, 0, 40),
#     Course("PSY205", "PSY", 200, 0, 0, 40),
#     Course("PSY209", "PSY", 200, 0, 0, 40),
#     Course("PSY308", "PSY", 300, 1, 0, 20),
#
#     # Social Studies
#     Course("SOCI102", "SOCI", 100, 0, 0, 70),  # What the fuck is this course? Originally this course capacity is 80
#     Course("SOCI105", "SOCI",100, 0, 0, 50),
#     Course("SOCI109", "SOCI",100, 0, 0, 50),
#     Course("SOCI211", "SOCI",200,0,0,40),
#     Course("SOCI219","SOCI",200, 0, 0, 40),
#
#     # Vietnam Studies
#     Course("VS106", "VS", 100, 1, 0, 50),
#     Course("VS208", "VS", 200, 0, 0, 40),
#     Course("VS213", "VS", 200, 0, 0, 40),
#     Course("VS214", "VS", 200, 1, 0, 20),
#     Course("VS305", "VS", 300, 1, 0, 30),
#     Course("VS306", "VS", 300, 0, 0, 30),
#
#     # Global Humanities and Social Changes
#     Course("CORE101", "CORE", 100, 0, 0, 18),
#     Course("CORE101", "CORE", 100, 0, 0, 18),
#     Course("CORE101", "CORE", 100, 0, 0, 18),
#     Course("CORE101", "CORE", 100, 0, 0, 18),
#     Course("CORE101", "CORE", 100, 0, 0, 18),
#     Course("CORE101", "CORE", 100, 0, 0, 18),
#     Course("CORE101", "CORE", 100, 0, 0, 18),
#     Course("CORE101", "CORE", 100, 0, 0, 18),
#     Course("CORE101", "CORE", 100, 0, 0, 18),
#     Course("CORE101", "CORE", 100, 0, 0, 18),
#
#     # Quantitative Reasoning for a Digital Age
#     Course("CORE103", "CORE", 100, 0, 0, 30),
#     Course("CORE103", "CORE", 100, 0, 0, 30),
#     Course("CORE103", "CORE", 100, 0, 0, 30),
#     Course("CORE103", "CORE", 100, 0, 0, 30),
#
#     # Scientific Enquiry
#     Course("CORE104", "CORE", 100, 0, 0, 30),
#     Course("CORE104", "CORE", 100, 0, 0, 30),
#     Course("CORE104", "CORE", 100, 0, 0, 30),
#     Course("CORE104", "CORE", 100, 0, 0, 30),
#     Course("CORE104", "CORE", 100, 0, 0, 30),
#
#     # Design and System Thinking
#     Course("CORE105", "CORE", 100, 0, 0, 25),
#     Course("CORE105", "CORE", 100, 0, 0, 25),
#     Course("CORE105", "CORE", 100, 0, 0, 25),
#     Course("CORE105", "CORE", 100, 0, 0, 25),
# ]

courses = [
    # Spring 2024

    # Applied Maths
    Course("MATH104", "MATH", 100, 0, 0, 50),
    Course("MATH201", "MATH", 200, 0, 0, 40),
    Course("MATH202", "MATH", 200, 1, 0, 40),
    Course("MATH306", "MATH", 300, 1, 0, 30),
    Course("MATH307", "MATH", 300, 0, 0, 30),
    Course("MATH310", "MATH", 300, 0, 0, 30),
    Course("MATH311", "MATH", 300, 1, 0, 30),

    # Arts and Media Studies
    Course("ARTS101", "ARTS", 100, 0, 0, 50),
    Course("ARTS104", "ARTS", 100, 0, 0, 25),
    Course("ARTS106", "ARTS", 100, 0, 0, 30),
    Course("ARTS107", "ARTS", 100, 1, 0, 30),
    Course("ARTS203", "ARTS", 200, 0, 0, 40),
    Course("ARTS209", "ARTS", 200, 1, 0, 25),
    Course("ARTS214", "ARTS", 200, 1, 0, 40),
    Course("ARTS302", "ARTS", 300, 1, 0, 25),
    Course("ARTS312", "ARTS", 300, 1, 0, 25),

    # Computer Science
    Course("CS201", "CS", 200, 0, 0, 40),
    Course("CS204", "CS", 200, 1, 0, 40),
    Course("CS205", "CS", 200, 0, 0, 40),
    Course("CS208", "CS", 200, 1, 0, 40),
    Course("CS312", "CS", 300, 0, 0, 30),

    # Economics
    Course("ECON201", "ECON", 200, 0, 0, 65),
    Course("ECON203", "ECON", 200, 0, 0, 65),
    Course("ECON211", "ECON", 200, 0, 0, 40),
    Course("ECON212", "ECON", 200, 0, 0, 40),
    Course("ECON307", "ECON", 300, 0, 0, 40),
    Course("ECON309", "ECON", 300, 1, 0, 30),

    # Engineer
    Course("ENG104", "ENG", 100, 0, 0, 30),
    Course("ENG207", "ENG", 200, 0, 0, 30),
    Course("ENG208", "ENG", 200, 0, 0, 30),
    Course("ENG209", "ENG", 200, 0, 0, 30),
    Course("ENG301", "ENG", 300, 0, 0, 30),
    Course("ENG309", "ENG", 300, 0, 0, 30),
    Course("ENG310", "ENG", 300, 0, 0, 30),

    # History
    Course("HIS104", "HIS", 100, 0, 0, 50),
    Course("HIS108", "HIS", 100, 0, 0, 50),
    Course("HIS200", "HIS", 200, 0, 0, 40),
    Course("HIS214", "HIS", 200, 0, 0, 40),
    Course("HIS215", "HIS", 200, 0, 0, 40),
    Course("HIS305", "HIS", 300, 0, 0, 30),
    Course("HIS309", "HIS", 300, 0, 0, 30),

    # Integrated Science
    Course("IS101", "IS", 100, 0, 0, 50),
    Course("IS103", "IS", 100, 0, 0, 50),
    Course("IS106", "IS", 100, 0, 0, 50),
    Course("IS209", "IS", 200, 0, 0, 25),
    Course("IS214", "IS", 200, 1, 0, 15),
    Course("IS302", "IS", 300, 0, 0, 10),
    Course("IS308", "IS", 300, 0, 0, 30),
    Course("IS309", "IS", 300, 0, 0, 10),

    # Literature
    Course("LIT104", "LIT", 100, 0, 0, 50),
    Course("LIT201", "LIT", 200, 0, 0, 40),
    Course("LIT210", "LIT", 200, 0, 0, 40),
    Course("LIT211", "LIT", 200, 0, 0, 40),
    Course("LIT312", "LIT", 300, 0, 0, 30),

    # Music
    Course("MUSC104", "MUSC", 100, 0, 0, 60),

    # Psychology
    Course("PSY101", "PSY", 100, 1, 0, 50),
    Course("PSY210", "PSY", 200, 1, 0, 40),
    Course("PSY301", "PSY", 300, 1, 0, 30),
    Course("PSY302", "PSY", 300, 1, 0, 30),
    Course("PSY305", "PSY", 300, 0, 0, 30),
    Course("PSY307", "PSY", 300, 1, 0, 30),
    Course("PSY309", "PSY", 300, 1, 0, 30),
    Course("PSY310", "PSY", 300, 1, 0, 30),

    # Social Studies
    Course("SOCI102", "SOCI", 100, 0, 0, 50),
    Course("SOCI105", "SOCI", 100, 0, 0, 50),
    Course("SOCI110", "SOCI", 100, 0, 0, 50),
    Course("SOCI216", "SOCI", 200, 0, 0, 25),
    Course("SOCI218", "SOCI", 200, 1, 0, 40),
    Course("SOCI305", "SOCI", 300, 0, 0, 30),
    Course("SOCI311", "SOCI", 300, 1, 0, 30),
    Course("SOCI312", "SOCI", 300, 0, 0, 30),
    Course("SOCI314", "SOCI", 300, 0, 0, 30),
    Course("SOCI315", "SOCI", 300, 0, 0, 30),
    Course("SOCI316", "SOCI", 300, 1, 0, 30),

    # Vietnam Studies
    Course("VS110", "VS", 100, 1, 0, 50),
    Course("VS205", "VS", 200, 0, 0, 40),
    Course("VS211", "VS", 200, 1, 0, 40),
    Course("VS217", "VS", 200, 0, 0, 40),

    # Modern Vietnamese Culture and Society
    Course("CORE102", "CORE", 100, 0, 0, 30),
    Course("CORE102", "CORE", 100, 0, 0, 30),
    Course("CORE102", "CORE", 100, 0, 0, 30),
    Course("CORE102", "CORE", 100, 0, 0, 30),
    Course("CORE102", "CORE", 100, 0, 0, 30),
    Course("CORE102", "CORE", 100, 0, 0, 30),

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

    # Design and System Thinking
    Course("CORE105", "CORE", 100, 0, 0, 30),
    Course("CORE105", "CORE", 100, 0, 0, 30),
    Course("CORE105", "CORE", 100, 0, 0, 30),
    Course("CORE105", "CORE", 100, 0, 0, 30),
]