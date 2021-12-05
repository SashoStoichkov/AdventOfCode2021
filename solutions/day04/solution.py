#!/usr/bin/env python3
# Path: solutions/day04/solution.py
import os

# Read the input file
with open("input.txt", "r") as f:
    input_data = f.read()
    input_data = input_data.split("\n")
    input_data = [line.split(" -> ") for line in input_data]
    # make every element in a sublist a tuple
    input_data = [(line[0].split(","), line[1].split(",")) for line in input_data]
    # make every string in a sublist a int
    input_data = [[(int(x), int(y)) for x, y in line] for line in input_data]


def find_max_value(input_data):
    max_value = 0

    for line in input_data:
        for x, y in line:
            if x > max_value:
                max_value = x
            if y > max_value:
                max_value = y

    return max_value


# Write your solution here
def solution_part_1(input_data):
    max_value = find_max_value(input_data)
    grid = [["." for x in range(max_value + 1)] for y in range(max_value + 1)]

    for line in input_data:
        x1 = line[0][0]
        y1 = line[0][1]
        x2 = line[1][0]
        y2 = line[1][1]

        if x1 == x2:
            for y in range(min((y1, y2)), max((y1, y2)) + 1):
                if grid[y][x1] == ".":
                    grid[y][x1] = 0
                grid[y][x1] += 1
        elif y1 == y2:
            for x in range(min((x1, x2)), max((x1, x2)) + 1):
                if grid[y1][x] == ".":
                    grid[y1][x] = 0
                grid[y1][x] += 1

    # count all elements in the grid that have a value greater than 1
    count = 0

    for x in range(max_value + 1):
        for y in range(max_value + 1):
            if grid[y][x] != "." and grid[y][x] > 1:
                count += 1

    print("Part 1:", count)


def solution_part_2(input_data):
    max_value = find_max_value(input_data)
    grid = [["." for x in range(max_value + 1)] for y in range(max_value + 1)]

    for line in input_data:
        x1 = line[0][0]
        y1 = line[0][1]
        x2 = line[1][0]
        y2 = line[1][1]

        if x1 == x2:
            for y in range(min((y1, y2)), max((y1, y2)) + 1):
                if grid[y][x1] == ".":
                    grid[y][x1] = 0
                grid[y][x1] += 1
        elif y1 == y2:
            for x in range(min((x1, x2)), max((x1, x2)) + 1):
                if grid[y1][x] == ".":
                    grid[y1][x] = 0
                grid[y1][x] += 1
        else:
            xs = range(x1, x2 + 1) if x1 < x2 else range(x1, x2 - 1, -1)
            ys = range(y1, y2 + 1) if y1 < y2 else range(y1, y2 - 1, -1)

            for x, y in zip(xs, ys):
                if grid[y][x] == ".":
                    grid[y][x] = 0
                grid[y][x] += 1

    # count all elements in the grid that have a value greater than 1
    count = 0

    for x in range(max_value + 1):
        for y in range(max_value + 1):
            if grid[y][x] != "." and grid[y][x] > 1:
                count += 1

    print("Part 2:", count)


if __name__ == "__main__":
    solution_part_1(input_data)
    solution_part_2(input_data)
