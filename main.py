from time import time
from algorithm import *
from schedule import *

def print_schedule(solution: Schedule):
    for day in week_schedule:
        print('\n')
        print('\n')
        print(f"{week_schedule[day].upper()}")
        for time_slot in time_schedule:
            print("\n\n" + time_schedule[time_slot])
            for classroom in classrooms:
                print(f"\n{classroom}", end="\t")
                for i in range(len(solution.lessons)):
                    if (
                            solution.times[i].weekday == day
                            and solution.times[i].time == time_slot
                            and solution.classrooms[i].room == classroom.room
                    ):
                        print(solution.lessons[i], end="")

if __name__ == "__main__":
    start_time = time()
    benchmark_minimum_remaining_values()
    print(f"Minimum Remaining Values time execution: {time() - start_time} seconds")

    start_time = time()
    benchmark_least_constraining_value()
    print(f"Least Constraining Value time execution: {time() - start_time} seconds")

    start_time = time()
    benchmark_degree_heuristic()
    print(f"Degree Heuristic time execution: {time() - start_time} seconds")

    start_time = time()
    benchmark_forward_checking()
    print(f"Forward Checking time execution: {time() - start_time} seconds")

    optimal_schedule = Schedule([], [], [])
    backtrack(forward_checking, setup_domains(), optimal_schedule)
    print_schedule(optimal_schedule)
