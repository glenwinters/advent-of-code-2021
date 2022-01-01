#!/usr/bin/env python3


def read_input(filename):
    with open(f"./{filename}") as f:
        lines = f.read().splitlines()
        return lines


def a(nums):
    count = 0
    for i in range(len(nums)):
        if i == 0:
            continue
        elif nums[i] > nums[i - 1]:
            count += 1
            # print(f"{nums[i]} increased - {count}")
        # else:
        #   print(f"{nums[i]} decreased - {count}")

    print(count)


def b(nums):
    count = 0
    last = 0
    for i in range(len(nums)):
        if i == 0 or i == 1:
            continue

        total = nums[i] + nums[i - 1] + nums[i - 2]
        # print(total)

        if last != 0 and total > last:
            # print("bump")
            count += 1

        last = total
    print(count)


if __name__ == "__main__":
    lines = read_input("input.txt")
    nums = [int(line) for line in lines]
    a(nums)
    b(nums)
