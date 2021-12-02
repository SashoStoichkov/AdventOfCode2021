#!/usr/bin/env python3
# Path: solutions/day01/solution.py
import os

# Read the input file
with open("input.txt", "r") as f:
    input_data = f.read()

# Write your solution here
def solution_part_1(input_data):
    commands = input_data.split("\n")

    horizontal = 0
    depth = 0

    for command in commands:
        c = command.split(" ")
        c[1] = int(c[1])

        if c[0] == "forward":
            horizontal += c[1]
        elif c[0] == "down":
            depth += c[1]
        elif c[0] == "up":
            depth -= c[1]

    print("Part 1:", horizontal * depth)

def solution_part_2(input_data):
    commands = input_data.split("\n")

    horizontal = 0
    depth = 0
    aim = 0

    for command in commands:
        c = command.split(" ")
        c[1] = int(c[1])

        if c[0] == "forward":
            horizontal += c[1]
            depth += (aim * c[1])
        elif c[0] == "down":
            aim += c[1]
        elif c[0] == "up":
            aim -= c[1]

    print("Part 2:", horizontal * depth)


if __name__ == "__main__":
    solution_part_1(input_data)
    solution_part_2(input_data)
