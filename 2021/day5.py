import numpy as np
from aocd.models import Puzzle


def parse(raw):
    raw = raw.split()

    vorh = []
    diag = []
    for i in range(int(len(raw) / 3)):
        vent = raw[i * 3:i * 3 + 3]

        p1 = list(map(int, vent[0].split(',')))
        p2 = list(map(int, vent[2].split(',')))

        # check if horizonal or vertical
        if p1[0] == p2[0] or p1[1] == p2[1]:
            vorh.append([p1[0], p1[1], p2[0], p2[1]])
        else:
            diag.append([p1[0], p1[1], p2[0], p2[1]])

    return np.array(vorh), np.array(diag)


def calculate_danger(vents):
    maxloc = vents.max()
    ventmap = np.zeros((maxloc + 1, maxloc + 1))

    # populate ventmap
    for v in vents:

        # if horizontal
        if v[0] == v[2]:
            if v[1] < v[3]:
                ventmap[v[0], v[1]:v[3] + 1] = ventmap[v[0], v[1]:v[3] + 1] + 1

            else:
                ventmap[v[0], v[3]:v[1] + 1] = ventmap[v[0], v[3]:v[1] + 1] + 1


        # if vertical
        elif v[1] == v[3]:
            if v[0] < v[2]:
                ventmap[v[0]:v[2] + 1, v[1]] = ventmap[v[0]:v[2] + 1, v[1]] + 1

            else:
                ventmap[v[2]:v[0] + 1, v[1]] = ventmap[v[2]:v[0] + 1, v[1]] + 1

        # diagonal
        else:
            # path x
            if v[2] > v[0]:
                pathx = range(v[0], v[2]+1)
            else:
                pathx = range(v[0], v[2]-1, -1)

            # path y
            if v[3] > v[1]:
                pathy = range(v[1], v[3]+1)
            else:
                pathy = range(v[1], v[3]-1, -1)

            for i, j in zip(pathx, pathy):
                ventmap[i, j] = ventmap[i, j] + 1

    # get 2+ values on ventmap
    danger = len(ventmap[ventmap >= 2])

    return danger


if __name__ == '__main__':
    # import unique puzzle data
    puzzle = Puzzle(2021, 5)

    vorh, diag = parse(puzzle.input_data)

    testv, testd = parse(
        "0,9 -> 5,9\n8,0 -> 0,8\n9,4 -> 3,4\n2,2 -> 2,1\n7,0 -> 7,4\n6,4 -> 2,0\n0,9 -> 2,9\n3,4 -> 1,4\n0,0 -> 8,8\n5,5 -> 8,2")

    answer1 = calculate_danger(vorh)
    answer2 = calculate_danger(np.append(vorh, diag, axis=0))

    print(f'Part 1: {answer1}')
    print(f'Part 2: {answer2}')
