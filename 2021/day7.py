import numpy as np
from aocd.models import Puzzle


def minimize(locs):

    cost = np.zeros((max(locs) - min(locs)))

    for y in range(min(locs), max(locs)):
        cost[y] = sum(abs(locs - y))

    return min(cost)


def minimize2(locs):

    cost = np.zeros((max(locs) - min(locs)))

    for y in range(min(locs), max(locs)):
        dist = abs(locs - y)
        cost[y] = np.sum(np.floor(dist * (dist + 1) / 2))

    return min(cost)


if __name__ == "__main__":
    # import unique puzzle data
    puzzle = Puzzle(2021, 7)

    # parse input string into list of ints
    input = np.array(list((map(int, puzzle.input_data.split(",")))))

    test_input = np.array([16, 1, 2, 0, 4, 2, 7, 1, 2, 14])

    answer1 = minimize(input)
    answer2 = minimize2(input)

    print(f"Part 1: {answer1}")
    print(f"Part 2: {answer2}")
