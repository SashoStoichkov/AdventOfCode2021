#!/usr/bin/env python3
# Path: solutions/day09/solution.py
import os

# Read the input file
with open("input.txt", "r") as f:
    input_data = f.read()
    input_data = input_data.split("\n")
    input_data = [list(line) for line in input_data]


OPENING = ["(", "[", "{", "<"]
CLOSING = [")", "]", "}", ">"]
MATCHING = {"(": ")", "[": "]", "{": "}", "<": ">"}


def line_check(line):
    is_corrupted = False
    last_opening_brackets = []
    last_closing_bracket = None

    for bracket in line:
        if bracket in OPENING:
            last_opening_brackets.append(bracket)
        elif bracket in CLOSING:
            last_closing_bracket = bracket

        if last_closing_bracket is not None:
            last_opening_bracket = last_opening_brackets[-1]

            if MATCHING[last_opening_bracket] != last_closing_bracket:
                is_corrupted = True
                break
            else:
                last_opening_brackets.pop(-1)
                last_closing_bracket = None

    return [is_corrupted, last_opening_brackets, last_closing_bracket]


# Write your solution here
def solution(input_data):
    illegal_bracket_points = {")": 3, "]": 57, "}": 1197, ">": 25137}
    illegal_sum = 0

    completion_bracket_points = {")": 1, "]": 2, "}": 3, ">": 4}
    completion_values = []

    for line in input_data:
        check = line_check(line)

        if check[0]:
            illegal_sum += illegal_bracket_points[check[2]]
        else:
            closing_matching_brackets = []
            for bracket in check[1]:
                closing_matching_brackets.append(MATCHING[bracket])

            closing_matching_brackets.reverse()

            completion_value = 0
            for bracket in closing_matching_brackets:
                completion_value *= 5
                completion_value += completion_bracket_points[bracket]

            completion_values.append(completion_value)

    print("Part 1:", illegal_sum)
    print("Part 2:", sorted(completion_values)[len(completion_values) // 2])


if __name__ == "__main__":
    solution(input_data)
