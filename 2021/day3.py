import numpy as np
from aocd.models import Puzzle


def part1(raw):

    # convert bits to individual ints
    for i in range(len(raw)):
        raw[i] = [int(a) for a in str(raw[i])]

    # convert to a numpy array and transpose
    raw = np.asarray(raw).T

    gamma_str = ''
    for row in raw:
        b = np.bincount(row).argmax()
        gamma_str = gamma_str + str(b)

    # convert binary string to int
    gamma = int(gamma_str, 2)

    # make gamma string into numpy array and flip
    epsilon = 1 - np.asarray([int(a) for a in gamma_str])

    # convert binary to decimal
    epsilon = int("".join(str(x) for x in epsilon), 2)

    return gamma * epsilon


if __name__ == '__main__':
    # import unique puzzle data
    puzzle = Puzzle(2021, 3)

    # clean data
    raw = puzzle.input_data.split('\n')

    # run part 1
    answer1 = part1(raw)
    #
    # # run part 2
    # answer2 = part2(raw)
    #
    print(f'Part 1: {answer1}')
    # print(f'Part 2: {answer2}')
