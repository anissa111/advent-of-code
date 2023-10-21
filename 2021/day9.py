import numpy as np
from aocd.models import Puzzle


def parse(raw):
    input = [list(map(int, line)) for line in raw.split('\n')]
    return input


def part1(input):

    totalrisk = 0

    for i in range(len(input)):
        for j in range(len(input[0])):

            above = below = left = right = 10

            if i > 0:
                above = input[i - 1][j]
            if i < len(input) - 1:
                below = input[i + 1][j]
            if j > 0:
                left = input[i][j - 1]
            if j < len(input[0]) - 1:
                right = input[i][j + 1]

            # print(f'[{input[i][j]}]: {above} {below} {left} {right}')

            if input[i][j] < min([above, below, left, right]):
                totalrisk = totalrisk + input[i][j] + 1

    return totalrisk


if __name__ == '__main__':
    # import unique puzzle data
    puzzle = Puzzle(2021, 9)

    # parse input string into list of ints
    raw = puzzle.input_data

    test_raw = '''2199943210
3987894921
9856789892
8767896789
9899965678'''

    test_input = parse(test_raw)
    input = parse(raw)

    answer1 = part1(input)
    # answer2 = part2(test_input)

    print(f'Part 1: {answer1}')
    # print(f'Part 2: {answer2}')
