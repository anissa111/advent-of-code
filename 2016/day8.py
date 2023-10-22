from aocd.models import Puzzle
import numpy as np

puzzle = Puzzle(2016, 8)
raw = puzzle.input_data.split('\n')

# raw = [
#     'rect 3x2',
#     'rotate column x=1 by 1',
#     'rotate row y=0 by 4',
#     'rotate column x=1 by 1',
# ]


def display(lcd):
    for row in lcd:
        print(''.join(['█' if p else ' ' for p in row]))


def rect(lcd, a, b):
    lcd[0:b, 0:a] = 1
    return lcd


def rotate_row(lcd, y, dist):
    lcd[y, :] = np.roll(lcd[y, :], dist)
    return lcd


def rotate_column(lcd, x, dist):
    lcd[:, x] = np.roll(lcd[:, x], dist)
    return lcd


def follow_instructions(lcd, raw):
    for instruction in raw:
        instruction = instruction.split()

        match instruction:
            case ["rect", dims]:
                lcd = rect(lcd, *(int(x) for x in dims.split('x')))
            case ["rotate", "row", ystr, "by", dist]:
                lcd = rotate_row(lcd, int(ystr.split('=')[-1]), int(dist))
            case ["rotate", "column", xstr, "by", dist]:
                lcd = rotate_column(lcd, int(xstr.split('=')[-1]), int(dist))

    return lcd


def how_many_on(lcd):
    return int(sum(sum(lcd)))


lcd = np.zeros([6, 50])
# lcd = np.zeros([3, 7])
lcd = follow_instructions(lcd, raw)
part1 = how_many_on(lcd)
print(f'Part 1: {part1}')
display(lcd)
