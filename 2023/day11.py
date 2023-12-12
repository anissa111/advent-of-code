from aocd.models import Puzzle
import re
import numpy as np
from itertools import chain

puzzle = Puzzle(2023, 11)
data = puzzle.input_data.split('\n')
#data = puzzle.examples[0].input_data.split('\n')

def expand(n, data):
    rs = list(range(len(data)))
    cs = list(range(len(data[0])))

    for ri in range(len(data)):
        if len(re.findall('#', data[ri])) == 0:
            rs[ri+1:] = [i+n for i in rs[ri+1:]]

    dataT = [''.join(l)for l in np.array([[c for c in d] for d in data]).T.tolist()]

    for ci in range(len(dataT)):
        if len(re.findall('#', dataT[ci])) == 0:
            cs[ci+1:] = [i+n for i in cs[ci+1:]]

    galaxies = list(chain.from_iterable([[(i, m.start()) for m in re.finditer('#', data[i])] for i in range(len(data))]))

    galaxies = [(rs[r], cs[c]) for r, c in galaxies]

    return galaxies


def solve(galaxies):
    dist_sum = 0
    for i in range(len(galaxies)-1):
        dist_sum += sum([abs(galaxies[i][0]-x[0])+abs(galaxies[i][1]-x[1]) for x in galaxies[i+1:]])

    return dist_sum


print(f'Part 1: {solve(expand(1, data))}')
print(f'Part 2: {solve(expand(999_999, data))}')
