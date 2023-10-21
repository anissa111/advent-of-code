from aocd.models import Puzzle
import numpy as np

def decode(start, keypad, directions):
    curr = start
    for d in directions:
        curr = keypad[d][curr-1]

    return str(curr)

# import unique puzzle data
puzzle = Puzzle(2016, 2)
raw = puzzle.input_data.split()

# 1 2 3
# 4 5 6
# 7 8 9

keypad1 = {
    'U': [1,2,3,1,2,3,4,5,6],
    'D': [4,5,6,7,8,9,7,8,9],
    'L': [1,1,2,4,4,5,7,7,8],
    'R': [2,3,3,5,6,6,8,9,9]
}

start = 5

code1 = int(''.join([decode(start, keypad1, line) for line in raw]))
print("Part 1: " + str(code1))

