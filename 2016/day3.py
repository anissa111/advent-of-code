from aocd.models import Puzzle
import numpy as np

# get puzzle data
puzzle = Puzzle(2016, 3)
raw = puzzle.input_data.split("\n")

possible1 = 0
for tri in raw:
    # unpack
    a, b, c = (int(s) for s in tri.split())

    # check
    if (a + b > c) and (b + c > a) and (a + c > b):
        possible1 += 1

print("Part 1: " + str(possible1))

possible2 = 0
raw = np.array([[int(i) for i in l.split()] for l in raw]).T

# go through all columns
for vert in raw:
    for start in range(0, len(vert), 3):
        a, b, c = (vert[start], vert[start + 1], vert[start + 2])

        # check
        if (a + b > c) and (b + c > a) and (a + c > b):
            possible2 += 1

print("Part 2: " + str(possible2))
