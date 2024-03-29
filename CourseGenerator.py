import random


def restricted_time_slot_1h30():
    time_1h30 = []
    duration = 1.5
    for i in range(3):
        day = random.randint(0, 2)
        time = random.randint(0, 5)
        my_list = [(day, time, duration), (day + 2, time, duration)]
        time_1h30.append(my_list)
    return time_1h30


def restricted_time_slot_3h():
    time_3h = []
    duration = 3
    for i in range(3):
        day = random.randint(0, 4)
<<<<<<< HEAD
        time = random.randint(0, 4)
=======
        time = random.randint(0, 5)
>>>>>>> origin/linh
        time_3h.append([(day, time, duration)])
    return time_3h


def days_restricted_time_slot_1h30():
    time_1h30 = []
    day = random.randint(0, 2)
    duration = 1.5
    for i in range(6):
        my_list = [(day, i, duration), (day + 2, i, duration)]
        time_1h30.append(my_list)
    return time_1h30


def days_restricted_time_slot_3h():
    time_3h_day: list[list[tuple[int, int, int]]] = []
    day = random.randint(0, 4)
    duration = 3
    for i in range(5):
        time_3h_day.append([(day, i, duration)])
    return time_3h_day


def time_slot_1h30_free_all():
    time_free = []
    duration = 1.5
    for days in range(3):
        for times in range(6):
            time_free.append([(days, times, duration), (days + 2, times, duration)])
    return time_free


def time_slot_3h_free_all():
    time_free = []
    duration = 3
    for days in range(5):
        for times in range(5):
            time_free.append([(days, times, duration)])
    return time_free


def course_generator(restricted_1h30, restricted_3h, days_restricted_1h30, days_restricted_3h, free_1h30, free_3h):
    base = 100
    for i in range(1, restricted_1h30+1):
        base += 1
        print("Course(\"", end="")
        print(base, end="")
        print("\", ", end="")
        print(restricted_time_slot_1h30(), end="")
        print(", ", end="")
        print(random.randint(10, 50), end="")
        print("),")

    for i in range(1, restricted_3h+1):
        base += 1
        print("Course(\"", end="")
        print(base, end="")
        print("\", ", end="")
        print(restricted_time_slot_3h(), end="")
        print(", ", end="")
        print(random.randint(10, 50), end="")
        print("),")

    for i in range(1, days_restricted_1h30+1):
        base += 1
        print("Course(\"", end="")
        print(base, end="")
        print("\", ", end="")
        print(days_restricted_time_slot_1h30(), end="")
        print(", ", end="")
        print(random.randint(10, 50), end="")
        print("),")

    for i in range(1, days_restricted_3h+1):
        base += 1
        print("Course(\"", end="")
        print(base, end="")
        print("\", ", end="")
        print(days_restricted_time_slot_3h(), end="")
        print(", ", end="")
        print(random.randint(10, 50), end="")
        print("),")

    for i in range(1, free_1h30+1):
        base += 1
        print("Course(\"", end="")
        print(base, end="")
        print("\", ", end="")
        print(time_slot_1h30_free_all(), end="")
        print(", ", end="")
        print(random.randint(10, 50), end="")
        print("),")

    for i in range(1, free_3h):
        base += 1
        print("Course(\"", end="")
        print(base, end="")
        print("\", ", end="")
        print(time_slot_3h_free_all(), end="")
        print(", ", end="")
        print(random.randint(10, 50), end="")
        print("),")


def main():
    restricted_1h30 = 5
    restricted_3h = 5
    days_restricted_1h30 = 5
    days_restricted_3h = 5
    free_1h30 = 5
    free_3h = 5
    course_generator(restricted_1h30, restricted_3h, days_restricted_1h30, days_restricted_3h, free_1h30, free_3h)


if __name__ == "__main__":
    main()
