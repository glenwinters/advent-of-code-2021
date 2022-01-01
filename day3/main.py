#!/usr/bin/env python3


def get_input(filename):
    with open(f"./{filename}", "r") as f:
        return f.read().splitlines()


def a():
    lines = get_input("input.txt")

    gamma = ""
    epsilon = ""
    for i in range(len(lines[0])):
        ones = 0
        for j in range(len(lines)):
            if lines[j][i] == "1":
                ones += 1
        if ones > (len(lines) / 2):
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"
    # print(gamma)
    # print(epsilon)
    print(int(gamma, 2) * int(epsilon, 2))


def split(nums, i):
    """Splits nums by commonality of digit at index i"""
    ones = []
    zeroes = []
    for j in range(len(nums)):
        if nums[j][i] == "1":
            ones.append(nums[j])
        else:
            zeroes.append(nums[j])

    # print(len(ones), len(zeroes))
    if len(ones) >= len(zeroes):
        return ones, zeroes
    else:
        return zeroes, ones


def b():
    lines = get_input("input.txt")

    most = lines
    for i in range(len(lines[0])):
        most, _ = split(most, i)
        if len(most) == 1:
            break

    least = lines
    for i in range(len(lines[0])):
        _, least = split(least, i)
        if len(least) == 1:
            break

    oxygen = int(most[0], 2)
    co2 = int(least[0], 2)

    print(oxygen * co2)


if __name__ == "__main__":
    a()
    b()
