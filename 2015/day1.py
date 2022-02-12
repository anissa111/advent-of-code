import numpy as np
from aocd.models import Puzzle


def calc_floor(raw):

    floor = 0

    for e in [e for e in raw]:
        if e == '(':
            floor += 1
        elif e == ')':
            floor -= 1
    
    return floor

def find_basement(raw):
    
        floor = 0
        pos = 1

        for e in [e for e in raw]:
            if e == '(':
                floor += 1
            elif e == ')': 
                floor -= 1

            if floor < 0:
                return pos
            pos += 1


if __name__ == '__main__':

    # import unique puzzle data
    puzzle = Puzzle(2015, 1)
    raw = puzzle.input_data

    test_raw = ")())())"

    answer1 = calc_floor(raw)
    answer2 = find_basement(raw)

    print(f'Part 1: {answer1}')
    print(f'Part 2: {answer2}')
