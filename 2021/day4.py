import numpy as np
from aocd.models import Puzzle


def part1(input):
    print("paer 1")


def clean_input(raw):

    # get first row of input and separate by commas
    moves = raw.split()[0].split(',')

    # convert list of strings to list of ints
    moves = list(map(int, moves))

    # save back split without first moves row
    raw = raw.split()[1:]

    # get number of boards in input
    size = 5
    nboards = int(len(raw)/(size**2))   # will be 100

    # set up empty array for parsed boards
    boards = np.empty(shape=(nboards, size, size))
    for i in range(nboards):

        # parse next set of numbers into a 5x5
        board = np.reshape(raw[i*size**2:i*size**2+size**2], (size, size))

        # store parsed board
        boards[i] = board

    return moves, boards



if __name__ == '__main__':
    # import unique puzzle data
    puzzle = Puzzle(2021, 4)

    moves, boards = clean_input(puzzle.input_data)

    print("done")

