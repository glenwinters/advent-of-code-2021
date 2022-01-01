#!/usr/bin/env python3


def get_input(filename):
    with open(f"./{filename}", "r") as f:
        return f.read().splitlines()


def a():
    lines = get_input("input.txt")
    x = 0
    y = 0
    for line in lines:
        command, value_str = line.split()
        value = int(value_str)

        if command == "forward":
            x += value
        elif command == "down":
            y += value
        elif command == "up":
            y -= value
        else:
            raise Exception(f"Unknown command: {command}")

    print(x * y)


def b():
    lines = get_input("input.txt")
    x = 0
    y = 0
    aim = 0
    for line in lines:
        command, value_str = line.split()
        value = int(value_str)

        if command == "forward":
            x += value
            y += aim * value
        elif command == "down":
            aim += value
        elif command == "up":
            aim -= value
        else:
            raise Exception(f"Unknown command: {command}")

    print(x * y)


if __name__ == "__main__":
    a()
    b()
