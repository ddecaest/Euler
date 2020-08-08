import os
import functools


def calculate_score(name_input):
    score = 0
    for letter in name_input.lower():
        score += ord(letter) - 96
    return score


if __name__ == "__main__":
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../resources/p022_names.txt')
    file = open(filename, 'r')

    names = []
    lines = file.readlines()
    for line in lines:
        names += line.replace("\"", "").split(",")

    names.sort()

    tally = 0
    for index, name in enumerate(names):
        tally += calculate_score(name) * (index + 1)

    print(tally)
