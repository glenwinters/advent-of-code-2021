#!/usr/bin/env python3


def get_input():
    lines = open("./input.txt", "r").read().splitlines()
    start = [int(n) for n in lines[0].split(",")]
    return start


def print_timers(timers, zero):
    timer_count = len(timers)
    for i in range(len(timers)):
        print(timers[(zero + i) % timer_count], end="")
    print("")


def fish(steps):
    start = get_input()

    # Represents counts of fish at time 0, 1, 2, ... where the time
    # corresponds with the index
    # The index changes meaning based on zero_index
    zero_index = 0

    timers = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    timer_count = len(timers)

    # Populate timers
    for n in start:
        timers[n] += 1

    # print_timers(timers, zero_index)

    ticks = steps
    while ticks != 0:
        timers[(zero_index + 7) % timer_count] += timers[zero_index]
        zero_index = (zero_index + 1) % timer_count
        # print_timers(timers, zero_index)
        ticks -= 1

    print(sum(timers))


def a():
    fish(80)


def b():
    fish(256)


if __name__ == "__main__":
    a()
    b()
