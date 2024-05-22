import random

def course_generator(free_1h30, free_3h):
    majors = ['CORE', 'ART', 'LIT', 'VS', 'SOCI', 'ECON', 'HIS', 'PSY', 'ENG', 'IS', 'MATH', 'CS']
    levels = ['100', '200', '300']
    course_name_dict = {}

    with open('output_courses.txt', 'w') as f:

        for i in range(1, free_1h30+1):
            major = random.choice(majors)
            level = random.choice(levels)
            if major == 'CORE':
                level = '100'
            if not major+level in course_name_dict:
                course_name_dict[major+level] = 0
            course_name_dict[major+level] += 1
            course_name = major + level[:2] + str(course_name_dict[major+level])
            f.write(f'Course("{course_name}", "{major}", {level}, 0, 0, {10*random.randint(1, 5)}), \n')

        for i in range(1, free_3h):
            major = random.choice(majors)
            level = random.choice(levels)
            if major == 'CORE':
                level = '100'
            if not major+level in course_name_dict:
                course_name_dict[major+level] = 0
            course_name_dict[major + level] += 1
            course_name = major + level[:2] + str(course_name_dict[major + level])
            f.write(f'Course("{course_name}", "{major}", {level}, 1, 0, {10*random.randint(1, 5)}){"" if i==free_3h-1 else ","} \n')


def main():
    free_1h30 = 100
    free_3h = 50
    course_generator(free_1h30, free_3h)


if __name__ == "__main__":
    main()
