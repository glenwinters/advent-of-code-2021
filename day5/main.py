#!/usr/bin/env python3


from collections import defaultdict


def to_coord(s):
    x, y = s.split(",")
    return [int(x), int(y)]


def get_input():
    lines = open("./input.txt").read().splitlines()
    coords = []
    for line in lines:
        c1, c2 = line.split(" -> ")
        coords.append(to_coord(c1) + to_coord(c2))
    return coords


def a():
    input = get_input()

    hits = defaultdict(int)
    twoplus = 0
    for coords in input:
        x1, y1, x2, y2 = coords

        # Skip diagonals for now
        if x1 != x2 and y1 != y2:
            continue

        # For each pts in each land, add to hits and count up 2s
        # oops this is broken for diagonals
        for x in range(abs(x2 - x1) + 1):
            for y in range(abs(y2 - y1) + 1):
                xd = x if x2 - x1 > 0 else -x
                yd = y if y2 - y1 > 0 else -y
                key = f"{x1 + xd},{y1 + yd}"
                hits[key] += 1
                if hits[key] == 2:
                    twoplus += 1

    print(twoplus)


def sign(n):
    if n > 0:
        return 1
    elif n < 0:
        return -1
    else:
        return 0


def b():
    input = get_input()

    hits = defaultdict(int)
    twoplus = 0
    for coords in input:
        x1, y1, x2, y2 = coords

        # For each pts in each land, add to hits and count up 2s
        x = x1
        y = y1

        xd = sign(x2 - x1)
        yd = sign(y2 - y1)

        while x != x2 or y != y2:
            key = f"{x},{y}"
            hits[key] += 1
            if hits[key] == 2:
                twoplus += 1

            x = x + xd
            y = y + yd

        # awkwardly handle last number lol
        key = f"{x},{y}"
        hits[key] += 1
        if hits[key] == 2:
            twoplus += 1

    print(twoplus)


if __name__ == "__main__":
    a()
    b()
