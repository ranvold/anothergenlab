from collections import namedtuple

week_schedule = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday"}

time_schedule = {
    1: "8:40-10:15",
    2: "10:35-12:10",
    3: "12:20-13:55",
}

Classroom = namedtuple("Classroom", "room is_big")
Time = namedtuple("Time", "weekday time")
Teacher = namedtuple("Teacher", "name")
Subject = namedtuple("Subject", "name")
Group = namedtuple("Group", "name")
Lesson = namedtuple("Lesson", "teacher subject group is_lecture per_week")
Schedule = namedtuple("Schedule", "lessons classrooms times")

DomainEl = namedtuple("DomainEl", "day time room")

Classroom.__repr__ = lambda c: f"{c.room} ({'big' if c.is_big else 'small'})"
Teacher.__repr__ = lambda t: f"{t.name.split()[1]}"
Subject.__repr__ = lambda s: f"{s.name.split()[1]}"
Group.__repr__ = lambda g: f"{g.name}"

Lesson.__repr__ = (
    lambda lesson: f"{lesson.teacher} | {lesson.subject} | {lesson.group} | "
                   f"{'Lecture' if lesson.is_lecture else 'Seminar'}{lesson.per_week}/week"
)


def serialize(sch: Schedule):
    output = ""
    for i in range(len(sch.lessons)):
        output += f"{sch.lessons[i]}, {sch.classrooms[i]}, {sch.times[i]}\n"
    return output


Schedule.__repr__ = lambda sch: serialize(sch)

groups = [
    Group(name)
    for name in (
        "1 Cs-10",
        "2 Cs-11",
        "3 Cs-21",
        "4 Cs-22",
        "5 Cs-30",
    )
]

teachers = [
    Teacher(name)
    for name in (
        "0 Doctor-John",
        "1 Professor-Carrel",
        "2 Doctor-Rivera",
        "3 Professor-Irvine",
        "4 Doctor-Lloyd",
        "5 Professor-Fisher",
        "6 Doctor-Greene",
        "7 Professor-Piter",
        "8 Doctor-Irvine",
        "9 Professor-Douglas",
        "10 Doctor-Lux",
        "11 Professor-Ahri",
        "12 Doctor-Darius",
        "13 Professor-Jarvan",
        "14 Doctor-Jax",
        "15 Professor-Perry",
        "16 Doctor-Leona",
        "17 Professor-Vayne",
        "18 Doctor-Riven",
    )
]

classrooms = [
    Classroom(101, True),
    Classroom(102, True),
    Classroom(103, True),
    Classroom(1, False),
    Classroom(2, False),
    Classroom(3, False),
]

schedule = [
    Time(day, time_slot)
    for day in range(1, len(week_schedule.keys()) + 1)
    for time_slot in range(1, len(week_schedule.keys()) + 1)
]

subjects = [
    Subject(name)
    for name in (
        "0 Introduction-to-Computer-Science",
        "1 Business-Analysis",
        "2 Solution-Design",
        "3 Networking",
        "4 Operating-Systems",
        "5 Database",
        "6 Programming",
        "7 User-Interface-Design",
        "8 Programming-Language-Paradigms",
        "9 Information-Systems",
        "10 Computer-Algorithms",
        "11 Communications-Systems",
        "12 Application-Development",
        "13 Engineering-Graphics",
        "14 Electrical-Engineering",
        "15 Object-Oriented-Programming",
        "16 Data-Mining",
        "17 Discrete-Structures",
    )
]

lessons = [
    Lesson(teachers[0], subjects[0], groups[0], False, 1),
    Lesson(teachers[1], subjects[1], groups[0:5], True, 1),
    Lesson(teachers[2], subjects[2], groups[0], True, 2),
    Lesson(teachers[2], subjects[2], groups[0], True, 2),
    Lesson(teachers[3], subjects[12], groups[0], True, 1),
    Lesson(teachers[4], subjects[4], groups[0:5], True, 1),
    Lesson(teachers[5], subjects[4], groups[0], False, 1),
    Lesson(teachers[5], subjects[15], groups[0], True, 1),
    Lesson(teachers[9], subjects[6], groups[0:5], True, 1),
    Lesson(teachers[13], subjects[4], groups[0], False, 1),
    Lesson(teachers[13], subjects[16], groups[0], True, 2),
    Lesson(teachers[13], subjects[16], groups[0], True, 2),
    Lesson(teachers[5], subjects[4], groups[1], False, 1),
    Lesson(teachers[5], subjects[4], groups[2], False, 1),
    Lesson(teachers[6], subjects[4], groups[1], False, 1),
    Lesson(teachers[7], subjects[4], groups[2], False, 1),
    Lesson(teachers[8], subjects[3], groups[1:3], True, 1),
    Lesson(teachers[10], subjects[7], groups[1], False, 2),
    Lesson(teachers[10], subjects[7], groups[1], False, 2),
    Lesson(teachers[10], subjects[7], groups[2], False, 2),
    Lesson(teachers[10], subjects[7], groups[2], False, 2),
    Lesson(teachers[11], subjects[8], groups[1:3], True, 2),
    Lesson(teachers[11], subjects[8], groups[1:3], True, 2),
    Lesson(teachers[12], subjects[9], groups[1:3], True, 2),
    Lesson(teachers[12], subjects[9], groups[1:3], True, 2),
    Lesson(teachers[5], subjects[4], groups[3], False, 1),
    Lesson(teachers[5], subjects[4], groups[4], False, 1),
    Lesson(teachers[6], subjects[4], groups[3], False, 1),
    Lesson(teachers[6], subjects[4], groups[4], False, 1),
    Lesson(teachers[14], subjects[12], groups[3:5], True, 2),
    Lesson(teachers[14], subjects[12], groups[3:5], True, 2),
    Lesson(teachers[15], subjects[13], groups[3:5], False, 1),
    Lesson(teachers[16], subjects[11], groups[3:5], True, 2),
    Lesson(teachers[16], subjects[11], groups[3:5], True, 2),
    Lesson(teachers[17], subjects[14], groups[3:5], True, 1),
    Lesson(teachers[17], subjects[17], groups[3:5], True, 1),
    Lesson(teachers[18], subjects[10], groups[1:3], True, 1),
]
