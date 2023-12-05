from aocd.models import Puzzle
import numpy as np
import re
from itertools import chain
from math import prod

puzzle = Puzzle(2023, 5)

data = puzzle.input_data.split('\n\n')
#data = puzzle.examples[0].input_data.split('\n\n')

seeds = [int(s) for s in re.findall(r'\d+', data[0])]

layers = []
for i in range(1,len(data)):
    lmap = {}
    for l in data[i].split('\n')[1:]:
        l = [int(n) for n in list(re.findall(r'\d+', l))]
        #print(l)
        lmap[(l[1], l[1]+l[2])] = l[0]

    layers.append([lmap])

locs = []
for s in seeds:
    for l in layers:
        in_rs = [lr for lr in l[0] if lr[0]<=s<=lr[1]]
        if len(in_rs)>0:
            s = s-in_rs[0][0]+l[0][in_rs[0]]

    locs.append(s)

print(f'Part 1: {min(locs)}')

# new_seeds = list(chain.from_iterable([list(range(s1, s1+s2)) for s1, s2 in zip(seeds[::2], seeds[1::2])]))
# print(len(new_seeds))
# locs = []
# for s in new_seeds:
#     for l in layers:
#         in_rs = [lr for lr in l[0] if lr[0]<=s<=lr[1]]
#         if len(in_rs)>0:
#             s = s-in_rs[0][0]+l[0][in_rs[0]]

#     locs.append(s)

# print(f'Part 2: {min(locs)}')