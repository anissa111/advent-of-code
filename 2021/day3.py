import numpy as np
from aocd.models import Puzzle


def part1(input):
    gamma_str = ''
    for i in range(len(input[0])):
        b = most_common_bit(input, i)
        gamma_str = gamma_str + str(b)

    # convert binary string to int
    gamma = int(gamma_str, 2)

    # make gamma string into numpy array and flip
    epsilon = 1 - np.asarray([int(a) for a in gamma_str])

    # convert binary to decimal
    epsilon = int("".join(str(x) for x in epsilon), 2)

    return gamma * epsilon


def part2(input):
    inputmin = np.array(input)
    inputmax = np.array(input)

    # for every position
    for i in range(len(input[0])):
        bmax = most_common_bit(inputmax, i)

        inputmax = inputmax[np.where(np.transpose(inputmax)[i] == bmax)]

        if len(inputmax) == 1:
            break

    for i in range(len(input[0])):
        bmin = least_common_bit(inputmin, i)

        inputmin = inputmin[np.where(np.transpose(inputmin)[i] == bmin)]

        if len(inputmin) == 1:
            break

    oxygen = int("".join(str(x) for x in inputmax[0]), 2)
    co2 = int("".join(str(x) for x in inputmin[0]), 2)

    return oxygen * co2


def most_common_bit(input, position):
    # transpose
    inputT = np.transpose(np.asarray(input))
    b = np.bincount(inputT[position])

    if b[0] == b[1]:
        return 1

    return b.argmax()


def least_common_bit(input, position):
    # transpose
    inputT = np.transpose(np.asarray(input))
    b = np.bincount(inputT[position])

    if b[0] == b[1]:
        return 0

    return 1 - b.argmax()


if __name__ == '__main__':
    # import unique puzzle data
    puzzle = Puzzle(2021, 3)

    # clean data
    raw = puzzle.input_data.split('\n')
    # convert bits to individual ints
    for i in range(len(raw)):
        raw[i] = [int(a) for a in str(raw[i])]

    # run part 1
    answer1 = part1(raw)

    # run part 2
    answer2 = part2(raw)

    print(f'Part 1: {answer1}')
    print(f'Part 2: {answer2}')
