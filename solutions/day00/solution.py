#!/usr/bin/env python3
# Path: solutions/day00/solution.py
import os

# Read the input file
with open("input.txt", "r") as f:
    input_data = f.read()

# Write your solution here
def solution_part_1(input_data):
    data = input_data.split("\n")
    data = [int(x) for x in data]

    result = 0

    for i in range(len(data)):
        if i + 1 < len(data):
            if data[i] < data[i + 1]:
                result += 1

    print("Part 1 =", result)


def solution_part_2(input_data):
    data = input_data.split("\n")
    data = [int(x) for x in data]

    max_sets = len(data) - 2
    curr_set = 0

    sum_sets = []

    for i in range(len(data)):
        if curr_set == max_sets:
            break

        curr_sum = 0

        for j in range(3):
            if i + j < len(data):
                curr_sum += data[i + j]

        curr_set += 1
        sum_sets.append(curr_sum)
        i -= 2

    result = 0

    for i in range(len(sum_sets)):
        if i + 1 < len(sum_sets):
            if sum_sets[i] < sum_sets[i + 1]:
                result += 1

    print("Part 2 =", result)


if __name__ == "__main__":
    solution_part_1(input_data)
    solution_part_2(input_data)
