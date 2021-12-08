#!/usr/bin/env python3
# Path: solutions/day07/solution.py
import os, pprint

# Read the input file
with open("input.txt", "r") as f:
    input_data = f.read()

# Write your solution here
def solution_part_1(input_data):
    input_data = input_data.split("\n")
    input_data = [x.split(" | ") for x in input_data]
    input_data = [x[1].split(" ") for x in input_data]

    count = 0
    for line in input_data:
        for word in line:
            if len(word) in [2, 3, 4, 7]:
                count += 1

    print("Part 1:", count)


def output_to_digit(output, mapping):
    if len(output) == 2:
        return 1
    elif len(output) == 3:
        return 7
    elif len(output) == 4:
        return 4
    elif len(output) == 7:
        return 8
    else:
        indexes = sorted([mapping.index(x) for x in output])
        digit = None

        if indexes == [0, 1, 2, 4, 5, 6]:
            digit = 0
        elif indexes == [0, 2, 3, 4, 6]:
            digit = 2
        elif indexes == [0, 2, 3, 5, 6]:
            digit = 3
        elif indexes == [0, 1, 3, 5, 6]:
            digit = 5
        elif indexes == [0, 1, 3, 4, 5, 6]:
            digit = 6
        elif indexes == [0, 1, 2, 3, 5, 6]:
            digit = 9

        return digit


def solution_part_2(input_data):
    input_data = input_data.split("\n")
    input_data = [x.split(" | ") for x in input_data]

    signals = [sorted(x[0].split(" "), key=lambda y: len(y)) for x in input_data]
    outputs = [x[1].split(" ") for x in input_data]

    sum_of_outputs = 0

    for line_index in range(len(input_data)):
        mapping = [""] * 7
        mappings = [mapping] * 8

        for signal in signals[line_index]:
            if len(signal) == 2:
                for i in range(8):
                    if i in [0, 1, 4, 5]:
                        mappings[i] = ["", "", signal[0], "", "", signal[1], ""]
                    elif i in [2, 3, 6, 7]:
                        mappings[i] = ["", "", signal[1], "", "", signal[0], ""]

            elif len(signal) == 3:
                for i in range(8):
                    not_in_mapping = [x for x in signal if x not in mappings[i]]
                    mappings[i][0] = not_in_mapping[0]

            elif len(signal) == 4:
                for i in range(8):
                    not_in_mapping = [x for x in signal if x not in mappings[i]]
                    if i in [0, 2, 4, 6]:
                        mappings[i] = [
                            mappings[i][0],
                            not_in_mapping[0],
                            mappings[i][2],
                            not_in_mapping[1],
                            "",
                            mappings[i][5],
                            "",
                        ]
                    elif i in [1, 3, 5, 7]:
                        mappings[i] = [
                            mappings[i][0],
                            not_in_mapping[1],
                            mappings[i][2],
                            not_in_mapping[0],
                            "",
                            mappings[i][5],
                            "",
                        ]

            elif len(signal) == 7:
                for i in range(8):
                    not_in_mapping = [x for x in signal if x not in mappings[i]]
                    if i in [0, 1, 2, 3]:
                        mappings[i] = [
                            mappings[i][0],
                            mappings[i][1],
                            mappings[i][2],
                            mappings[i][3],
                            not_in_mapping[0],
                            mappings[i][5],
                            not_in_mapping[1],
                        ]
                    elif i in [4, 5, 6, 7]:
                        mappings[i] = [
                            mappings[i][0],
                            mappings[i][1],
                            mappings[i][2],
                            mappings[i][3],
                            not_in_mapping[1],
                            mappings[i][5],
                            not_in_mapping[0],
                        ]

        best_mapping = None
        for curr_mapping in mappings:
            count_valid = 0

            for signal in signals[line_index]:
                if output_to_digit(signal, curr_mapping) is not None:
                    count_valid += 1

            if count_valid == len(signals[line_index]):
                best_mapping = curr_mapping
                break

        curr_output = 0
        for output in outputs[line_index]:
            digit = output_to_digit(output, best_mapping)
            curr_output = curr_output * 10 + digit

        sum_of_outputs += curr_output

    print("Part 2:", sum_of_outputs)


if __name__ == "__main__":
    solution_part_1(input_data)
    solution_part_2(input_data)
