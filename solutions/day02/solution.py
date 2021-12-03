#!/usr/bin/env python3
# Path: solutions/day02/solution.py
import os
import copy

# Read the input file
with open("input.txt", "r") as f:
    input_data = f.read()

# Write your solution here
def solution_part_1(input_data):
    data = input_data.split("\n")

    gamma_rate = ""
    epsilon_rate = ""

    for i in range(len(data[0])):
        count_ones = 0
        count_zeros = 0

        for j in range(len(data)):
            if data[j][i] == "1":
                count_ones += 1
            elif data[j][i] == "0":
                count_zeros += 1

        if count_ones > count_zeros:
            gamma_rate += "1"
            epsilon_rate += "0"
        elif count_ones < count_zeros:
            gamma_rate += "0"
            epsilon_rate += "1"

    gamma = int(gamma_rate, 2)
    epsilon = int(epsilon_rate, 2)

    print("Part 1:", gamma * epsilon)


def most_common_bit(data, index):
    count_ones = 0
    count_zeros = 0

    for i in range(len(data)):
        if data[i][index] == "1":
            count_ones += 1
        elif data[i][index] == "0":
            count_zeros += 1

    if count_ones == len(data):
        return "11"
    elif count_zeros == len(data):
        return "00"
    elif count_ones >= count_zeros:
        return "1"
    elif count_ones < count_zeros:
        return "0"


def solution_part_2(input_data):
    data = input_data.split("\n")

    oxygen = copy.deepcopy(data)

    for i in range(len(oxygen[0])):
        mcb = most_common_bit(oxygen, i)

        if mcb == "1" or mcb == "11":
            oxygen = [x for x in oxygen if x[i] == "1"]
        elif mcb == "0" or mcb == "00":
            oxygen = [x for x in oxygen if x[i] == "0"]

    oxygen_rate = int(oxygen[0], 2)

    co2 = copy.deepcopy(data)

    for i in range(len(co2[0])):
        mcb = most_common_bit(co2, i)

        if mcb == "1" or mcb == "00":
            co2 = [x for x in co2 if x[i] == "0"]
        elif mcb == "0" or mcb == "11":
            co2 = [x for x in co2 if x[i] == "1"]

    co2_rate = int(co2[0], 2)

    print("Part 2:", oxygen_rate * co2_rate)


if __name__ == "__main__":
    solution_part_1(input_data)
    solution_part_2(input_data)
