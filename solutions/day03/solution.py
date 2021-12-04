#!/usr/bin/env python3
# Path: solutions/day03/solution.py
import os
import pprint

# Read the input file
with open("input.txt", "r") as f:
    input_data = f.read()

    data = input_data.split("\n")
    random_numbers = data[0].split(",")
    random_numbers = [int(x) for x in random_numbers]
    data.remove(data[0])
    boards = [x.split(" ") for x in data]
    # remove every "" from the list
    boards = [x for x in boards if x != [""]]
    # remove "" from every list
    boards = [[x for x in y if x != ""] for y in boards]
    # split the list into sublists of length 5
    boards = [boards[i : i + 5] for i in range(0, len(boards), 5)]
    # make every element in the list an integer
    boards = [[[int(x) for x in y] for y in z] for z in boards]
    # make every sublist a dictionary numbers as keys and booleans as values
    boards = [[{x: False for x in y} for y in z] for z in boards]

# Write your solution here
def solution_part_1(random_numbers, boards):
    win = False
    first_winning_board = None
    random_number = None

    for number in random_numbers:
        random_number = number

        for board in boards:
            for row in board:
                if number in row:
                    row[number] = True

        for board in boards:
            for column in zip(*board):
                column_dict = {x: board[column.index(x)][x] for x in column}
                if all(column_dict.values()):
                    first_winning_board = board
                    win = True
                    break

            for row in board:
                if all(row.values()):
                    first_winning_board = board
                    win = True
                    break

        if win:
            break

    sum_of_false = 0
    for row in first_winning_board:
        for number in row:
            if row[number] == False:
                sum_of_false += number

    print("Part 1:", sum_of_false * random_number)


def solution_part_2(random_numbers, boards):
    winning_boards = []
    random_number = None

    for number in random_numbers:
        random_number = number

        for board in boards:
            for row in board:
                if number in row:
                    row[number] = True

        for board in boards:
            winning_column = False
            winning_row = False

            for column in zip(*board):
                column_dict = {x: board[column.index(x)][x] for x in column}
                if all(column_dict.values()):
                    winning_boards.append((board, random_number))
                    boards.remove(board)
                    winning_column = True

            if winning_column:
                continue

            for row in board:
                if all(row.values()):
                    winning_boards.append((board, random_number))
                    boards.remove(board)
                    winning_row = True

            if winning_row:
                continue

    last_winning_board = winning_boards[-1]

    sum_of_false = 0
    for row in last_winning_board[0]:
        for number in row:
            if row[number] == False:
                sum_of_false += number

    print("Part 2:", sum_of_false * last_winning_board[1])


if __name__ == "__main__":
    solution_part_1(random_numbers, boards)
    solution_part_2(random_numbers, boards)
