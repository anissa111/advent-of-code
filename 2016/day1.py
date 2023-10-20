from aocd.models import Puzzle
import numpy as np

 # import unique puzzle data
puzzle = Puzzle(2016, 1)
raw = puzzle.input_data.split(', ')

# example data
#raw = "R5, L5, R5, R3".split(', ')

# rotational
rotate = {
    "L": np.array([[0, 1], [-1, 0]]),
    "R": np.array([[0, -1], [1, 0]])
}

# start pointing north at [0,0]
direction = [0, 1]
location = [0, 0]

for step in raw:
    direction = np.dot(direction, rotate[step[0]])
    location = location + direction*int(step[1:])

print("Part 1: " + str(sum(abs(location))))