from aocd.models import Puzzle
import numpy as np

def decode(start, keypad, directions, subs={}):
    curr = start
    for d in directions:
        curr = keypad[d][curr-1]

    if curr in subs:
        curr = subs[curr]

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

#     1
#   2 3 4
# 5 6 7 8 9
#   A B C
#     D

a, b, c, d = (10, 11, 12, 13)
keypad2 = {
    'U': [1,2,1,4,5,2,3,4,9,6,7,8,b],
    'D': [2,6,7,8,5,a,b,c,9,a,d,c,d],
    'L': [1,2,2,3,5,5,6,7,8,a,a,b,d],
    'R': [1,3,4,4,6,7,8,9,9,b,c,c,d]
}
subs = {10:'a', 11:'b', 12:'c', 13:'d'}

start = 5

code1 = int(''.join([decode(start, keypad1, line) for line in raw]))
print("Part 1: " + str(code1))

code2 =''.join([decode(start, keypad2, line, subs) for line in raw])
print("Part 2: " + str(code2))

