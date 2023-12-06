from sympy.solvers.solveset import solveset_real
from sympy.abc import x


def wait_for_it_1(times, distances):
    out = 1
    for time, dist in zip(times, distances):
        interval = solveset_real((x * (time - x)) > dist, x)
        interval = interval.evalf()

        interval_range = int(interval.end) - int(interval.start)
        out *= interval_range

    print(out)


def wait_for_it_2(times, distances):
    single_time = int("".join([str(n) for n in times]))
    single_dist = int("".join([str(n) for n in distances]))

    interval = solveset_real((x * (single_time - x)) > single_dist, x)
    interval = interval.evalf()

    interval_range = int(interval.end) - int(interval.start)
    print(interval_range)


if __name__ == '__main__':
    inp_file = open("boat_times", "r")

    times = [int(num.strip()) for num in inp_file.readline().split(":")[1].split()]
    distances = [int(num.strip()) for num in inp_file.readline().split(":")[1].split()]

    wait_for_it_1(times, distances)
    wait_for_it_2(times, distances)
