from Course import Course

courses = [
    Course("101", [[(1, 2, 3)], [(3, 0, 3)], [(1, 0, 3)]], 50),
    Course("102", [[(1, 3, 3)], [(3, 1, 3)], [(4, 3, 3)]], 40),
    Course("103", [[(2, 1, 1.5), (4, 1, 1.5)], [(2, 4, 1.5), (4, 4, 1.5)], [(0, 3, 1.5), (2, 3, 1.5)]], 10),
    Course("104", [[(2, 1, 1.5), (4, 1, 1.5)], [(0, 4, 1.5), (2, 4, 1.5)], [(1, 3, 1.5), (3, 3, 1.5)]], 50),
    Course("105", [[(0, 0, 1.5), (2, 0, 1.5)], [(0, 4, 1.5), (2, 4, 1.5)], [(2, 4, 1.5), (4, 4, 1.5)]], 50),
    Course("106", [[(1, 2, 1.5), (3, 2, 1.5)], [(1, 4, 1.5), (3, 4, 1.5)], [(0, 4, 1.5), (2, 4, 1.5)]], 20),
    Course("107", [[(2, 4, 1.5), (4, 4, 1.5)], [(0, 2, 1.5), (2, 2, 1.5)], [(2, 1, 1.5), (4, 1, 1.5)]], 40),
    Course("108", [[(1, 3, 1.5), (3, 3, 1.5)], [(0, 4, 1.5), (2, 4, 1.5)], [(2, 3, 1.5), (4, 3, 1.5)]], 40),
    Course("109", [[(1, 3, 3)], [(1, 2, 3)], [(1, 1, 3)]], 50),
    Course("110", [[(1, 4, 1.5), (3, 4, 1.5)], [(0, 4, 1.5), (2, 4, 1.5)], [(2, 3, 1.5), (4, 3, 1.5)]], 30),
    Course("111", [[(1, 2, 1.5), (3, 2, 1.5)], [(0, 0, 1.5), (2, 0, 1.5)], [(1, 0, 1.5), (3, 0, 1.5)]], 30),
    Course("112", [[(4, 2, 3)], [(1, 2, 3)], [(4, 2, 3)]], 30),
    Course("113", [[(2, 2, 1.5), (4, 2, 1.5)], [(1, 2, 1.5), (3, 2, 1.5)], [(0, 2, 1.5), (2, 2, 1.5)]], 10),
    Course("114", [[(4, 3, 3)], [(1, 0, 3)], [(1, 1, 3)]], 10),
    Course("115", [[(1, 4, 1.5), (3, 4, 1.5)], [(0, 0, 1.5), (2, 0, 1.5)], [(0, 2, 1.5), (2, 2, 1.5)]], 30),
    Course("116", [[(4, 0, 3)], [(2, 3, 3)], [(2, 1, 3)]], 10),
    Course("117", [[(2, 0, 1.5), (4, 0, 1.5)], [(0, 3, 1.5), (2, 3, 1.5)], [(1, 2, 1.5), (3, 2, 1.5)]], 50),
    Course("118", [[(1, 2, 1.5), (3, 2, 1.5)], [(2, 3, 1.5), (4, 3, 1.5)], [(0, 4, 1.5), (2, 4, 1.5)]], 10),
    Course("119", [[(0, 1, 3)], [(4, 2, 3)], [(1, 1, 3)]], 40),
    Course("120", [[(4, 2, 3)], [(3, 3, 3)], [(3, 2, 3)]], 20),
    Course("121", [[(3, 3, 3)], [(3, 3, 3)], [(0, 0, 3)]], 10),
    Course("122", [[(0, 3, 1.5), (2, 3, 1.5)], [(1, 4, 1.5), (3, 4, 1.5)], [(1, 3, 1.5), (3, 3, 1.5)]], 30),
    Course("123", [[(2, 0, 1.5), (4, 0, 1.5)], [(0, 3, 1.5), (2, 3, 1.5)], [(0, 0, 1.5), (2, 0, 1.5)]], 10),
    Course("124", [[(0, 1, 1.5), (2, 1, 1.5)], [(2, 0, 1.5), (4, 0, 1.5)], [(1, 4, 1.5), (3, 4, 1.5)]], 20),
    Course("125", [[(0, 0, 1.5), (2, 0, 1.5)], [(0, 4, 1.5), (2, 4, 1.5)], [(0, 1, 1.5), (2, 1, 1.5)]], 50),
    Course("126", [[(0, 3, 1.5), (2, 3, 1.5)], [(1, 4, 1.5), (3, 4, 1.5)], [(1, 1, 1.5), (3, 1, 1.5)]], 10),
    Course("127", [[(0, 3, 3)], [(2, 3, 3)], [(0, 0, 3)]], 20),
    Course("128", [[(2, 4, 1.5), (4, 4, 1.5)], [(2, 4, 1.5), (4, 4, 1.5)], [(1, 4, 1.5), (3, 4, 1.5)]], 30),
    Course("129", [[(2, 2, 1.5), (4, 2, 1.5)], [(1, 0, 1.5), (3, 0, 1.5)], [(1, 0, 1.5), (3, 0, 1.5)]], 20),
    Course("130", [[(3, 1, 3)], [(0, 3, 3)], [(2, 1, 3)]], 20),
    Course("131", [[(1, 3, 1.5), (3, 3, 1.5)], [(1, 2, 1.5), (3, 2, 1.5)], [(0, 1, 1.5), (2, 1, 1.5)]], 40),
    Course("132", [[(2, 0, 3)], [(2, 1, 3)], [(0, 1, 3)]], 10),
    Course("133", [[(1, 0, 1.5), (3, 0, 1.5)], [(2, 0, 1.5), (4, 0, 1.5)], [(1, 3, 1.5), (3, 3, 1.5)]], 30),
    Course("134", [[(1, 2, 1.5), (3, 2, 1.5)], [(2, 4, 1.5), (4, 4, 1.5)], [(2, 0, 1.5), (4, 0, 1.5)]], 30),
    Course("135", [[(4, 2, 3)], [(4, 2, 3)], [(4, 0, 3)]], 10),
    Course("136", [[(1, 3, 1.5), (3, 3, 1.5)], [(2, 2, 1.5), (4, 2, 1.5)], [(2, 4, 1.5), (4, 4, 1.5)]], 20),
    Course("137", [[(0, 1, 1.5), (2, 1, 1.5)], [(1, 4, 1.5), (3, 4, 1.5)], [(1, 4, 1.5), (3, 4, 1.5)]], 50),
    Course("138", [[(4, 1, 3)], [(0, 3, 3)], [(2, 2, 3)]], 40),
    Course("139", [[(0, 1, 3)], [(1, 0, 3)], [(1, 2, 3)]], 40),
    Course("140", [[(2, 2, 1.5), (4, 2, 1.5)], [(2, 1, 1.5), (4, 1, 1.5)], [(0, 4, 1.5), (2, 4, 1.5)]], 30),
    Course("141", [[(1, 3, 1.5), (3, 3, 1.5)], [(0, 1, 1.5), (2, 1, 1.5)], [(2, 1, 1.5), (4, 1, 1.5)]], 20),
    Course("142", [[(1, 2, 1.5), (3, 2, 1.5)], [(1, 4, 1.5), (3, 4, 1.5)], [(1, 1, 1.5), (3, 1, 1.5)]], 40),
    Course("143", [[(1, 4, 1.5), (3, 4, 1.5)], [(2, 2, 1.5), (4, 2, 1.5)], [(0, 4, 1.5), (2, 4, 1.5)]], 20),
    Course("144", [[(1, 0, 1.5), (3, 0, 1.5)], [(1, 2, 1.5), (3, 2, 1.5)], [(1, 1, 1.5), (3, 1, 1.5)]], 30),
    Course("145", [[(0, 1, 3)], [(3, 0, 3)], [(1, 2, 3)]], 50),
    Course("146", [[(0, 2, 1.5), (2, 2, 1.5)], [(1, 1, 1.5), (3, 1, 1.5)], [(1, 2, 1.5), (3, 2, 1.5)]], 40),
    Course("147", [[(0, 1, 1.5), (2, 1, 1.5)], [(1, 1, 1.5), (3, 1, 1.5)], [(2, 3, 1.5), (4, 3, 1.5)]], 30),
    Course("148", [[(1, 0, 1.5), (3, 0, 1.5)], [(0, 4, 1.5), (2, 4, 1.5)], [(0, 1, 1.5), (2, 1, 1.5)]], 30),
    Course("149", [[(2, 2, 1.5), (4, 2, 1.5)], [(2, 4, 1.5), (4, 4, 1.5)], [(0, 2, 1.5), (2, 2, 1.5)]], 40),
]

