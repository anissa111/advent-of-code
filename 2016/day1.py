from aocd.models import Puzzle
import numpy as np

 # import unique puzzle data
puzzle = Puzzle(2016, 1)
raw = puzzle.input_data.split(', ')

# shorter/example data
#raw = "R5, L5, R5, R3".split(', ')
#raw = "R8, R4, R4, R8".split(", ")
#raw = raw[:10]

# rotational
rotate = {
    "L": np.array([[0, 1], [-1, 0]]),
    "R": np.array([[0, -1], [1, 0]])
}

# start pointing north at [0,0]
direction = np.array([0, 1])
location = np.array([0, 0])
history = set([tuple(location)])
found = False

print(history)


for step in raw:
    dist = int(step[1:])
    direction = np.dot(direction, rotate[step[0]])

    # add all steps to memory
    if not found:
        for i in range(dist):
            s = location + direction*(i+1)
            if tuple(s) in history:
                print("Part 2: " + str(sum(abs(s))))
                found = True
            else:
                history.add(tuple(s))


    # update location
    location = location + direction*dist

print("Part 1: " + str(sum(abs(location))))