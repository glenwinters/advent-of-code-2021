#!/usr/bin/env python3

import statistics


def get_input():
    return open("./input.txt").read().splitlines()


def fuel(nums, target):
    return sum(abs(n - target) for n in nums)


def fuelb(nums, target):
    return sum(sum(range(abs(n - target) + 1)) for n in nums)


def a():
    lines = get_input()
    nums = [int(n) for n in lines[0].split(",")]
    target = int(statistics.median(nums))
    print(fuel(nums, target))


def b():
    lines = get_input()
    nums = [int(n) for n in lines[0].split(",")]
    target = int(statistics.mean(nums))
    print(fuelb(nums, target))


if __name__ == "__main__":
    a()
    b()
