#!/usr/bin/env python3
# Path: solutions/day06/solution.py
import os

# Read the input file
with open("input.txt", "r") as f:
    input_data = f.read()
    input_data = input_data.split(",")
    input_data = [int(x) for x in input_data]

# Write your solution here
def get_fuel(number, part):
    if part == 1:
        return number
    else:
        return (number * (number + 1)) // 2


def solution(input_data, part):
    fuel_array = []

    for i in range(max(input_data)):
        fuel_sum = 0

        for p in input_data:
            fuel_sum += get_fuel(abs(p - i), part)

        fuel_array.append(fuel_sum)

    print(f"Part {part}: {min(fuel_array)}")


if __name__ == "__main__":
    solution(input_data, 1)
    solution(input_data, 2)
