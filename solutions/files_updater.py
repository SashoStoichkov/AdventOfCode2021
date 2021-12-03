import os


def create_folders(n):
    for i in range(n):

        if i < 10:
            i = "0" + str(i)
        else:
            i = str(i)

        # create folder
        os.mkdir("day" + i)

        # create files in each folder
        with open("day" + i + "/" + "task" + ".md", "w") as f:
            f.write("# Task " + i)

        open("day" + i + "/" + "input" + ".txt", "w").close()

        with open("day" + i + "/" + "solution" + ".py", "w") as f:
            f.write("#!/usr/bin/env python3\n")
            f.write("# Path: solutions/day" + i + "/solution.py\n")
            f.write("import os\n\n")
            f.write("# Read the input file\n")
            f.write("with open(\"input.txt\", \"r\") as f:\n")
            f.write("    input_data = f.read()\n\n")
            f.write("# Write your solution here\n")
            f.write("def solution(input_data):\n")
            f.write("    pass\n\n\n")
            f.write("if __name__ == \"__main__\":\n")
            f.write("    solution(input_data)\n")


def rename_md_files(n):
    for i in range(2, n):

        if i < 10:
            i = "0" + str(i)
        else:
            i = str(i)

        # rename files
        os.rename("day" + i + "/" + "task" + ".md", "day" + i + "/" + "README" + ".md")


def change_contents_of_md_files(n):
    for i in range(3, n):

        if i < 10:
            i = "0" + str(i)
        else:
            i = str(i)

        # change contents of files
        with open("day" + i + "/" + "README" + ".md", "w") as f:
            f.write("# Day " + i + "\n\n")
            f.write("## Part One\n\n")
            f.write("## Part Two\n")


if __name__ == "__main__":
    # create_folders(25)
    # rename_md_files(25)
    # change_contents_of_md_files(25)
    pass
