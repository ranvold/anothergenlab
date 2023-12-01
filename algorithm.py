from copy import copy
from schedule import *


def setup_domains():
    domain = {}
    buf = []
    buf_lecture = []
    for day in week_schedule.keys():
        for time_slot in time_schedule.keys():
            for room in classrooms:
                buf.append(DomainEl(day, time_slot, room))
                if room.is_big:
                    buf_lecture.append(DomainEl(day, time_slot, room))
    for i in range(len(lessons)):
        if lessons[i].is_lecture:
            domain[i] = copy(buf_lecture)
        else:
            domain[i] = copy(buf)
    return domain


def update_domain(domain, lesson, day, time, room):
    for key in domain:
        buf = []
        for value in domain[key]:
            if not (value.day == day and value.time == time and value.room == room) and not (
                    value.day == day and value.time == time and (
                    lessons[key].teacher == lesson.teacher or set(map(str, lessons[key].group)) & set(
                map(str, lesson.group)))): buf.append(value)
            domain[key] = buf
    return domain


def backtrack(heuristic, domain, optimal_schedule):
    if not domain:
        return optimal_schedule
    index = heuristic(domain)
    if index == -1:
        return None
    for value in domain[index]:
        sch_copy = copy(optimal_schedule)
        sch_copy.times.append(Time(value.day, value.time))
        sch_copy.classrooms.append(value.room)
        sch_copy.lessons.append(lessons[index])
        dom_copy = copy(domain)
        dom_copy.pop(index)
        dom_copy = update_domain(dom_copy, lessons[index], value.day,
                                 value.time, value.room)
        res = backtrack(heuristic, dom_copy, sch_copy)
        if res:
            return res
    return None


def least_constraining_value(domain):
    counts = {}
    for i in domain:
        counts[i] = 0
        for key in domain:
            if i == key:
                continue

            for value in domain[key]:
                if not (
                        value.day == domain[i][0].day
                        and value.time == domain[i][0].time
                        and value.room == domain[i][0].room
                ) and not (
                        value.day == domain[i][0].day
                        and value.time == domain[i][0].time
                        and (
                                lessons[key].teacher == lessons[i].teacher
                                or set(map(str, lessons[key].group))
                                & set(map(str, lessons[i].group))
                        )
                ): counts[i] += 1

    index = list(counts.keys())[0]
    max_value = 0
    for key, value in counts.items():
        if value > max_value:
            max_value = value
            index = key
    return index


def degree_heuristic(domain):
    counts = {}
    for key in domain:
        counts[key] = 0 if lessons[key].is_lecture else 1
        for i in domain:
            if i == key:
                continue

            if lessons[key].teacher == lessons[i].teacher:
                counts[key] += 1
            counts[key] += len(
                set(map(str, lessons[key].group)) & set(map(str, lessons[i].group))
            )
        index = list(counts.keys())[0]
        max_value = 0

    for key, value in counts.items():
        if value > max_value:
            max_value = value
        index = key
    return index


def minimum_remaining_values(domain):
    min_length = len(week_schedule) * len(classrooms) * len(time_schedule) * 2
    index = list(domain.keys())[0]
    for key, value in domain.items():
        if len(value) < min_length:
            min_length = len(value)
            index = key
    return index


def forward_checking(domain):
    return list(domain.keys())[0]


def benchmark_least_constraining_value():
    return backtrack(least_constraining_value, setup_domains(), Schedule([], [], []))


def benchmark_degree_heuristic():
    return backtrack(degree_heuristic, setup_domains(), Schedule([], [], []))


def benchmark_minimum_remaining_values():
    return backtrack(minimum_remaining_values, setup_domains(), Schedule([], [], []))


def benchmark_forward_checking():
    return backtrack(forward_checking, setup_domains(), Schedule([], [], []))
