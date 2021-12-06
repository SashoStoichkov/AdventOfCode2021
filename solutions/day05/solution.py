#!/usr/bin/env python3
# Path: solutions/day05/solution.py
import os

# Read the input file
with open("input.txt", "r") as f:
    input_data = f.read()
    input_data = input_data.split(",")
    input_data = [int(x) for x in input_data]

# Write your solution here
def solution(input_data, days, part):
    digit_array = [0] * 9
    for num in input_data:
        digit_array[num] += 1

    for i in range(days):
        temp_array = digit_array[1:]
        temp_array.append(digit_array[0])
        temp_array[6] += digit_array[0]
        digit_array = temp_array

    print(f"Part {part}: {sum(digit_array)}")


if __name__ == "__main__":
    solution(input_data, 80, 1)
    solution(input_data, 256, 2)
