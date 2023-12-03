from aocd.models import Puzzle
import numpy as np
import re
from itertools import chain
from math import prod

puzzle = Puzzle(2023, 3).input_data.split('\n')
#puzzle = Puzzle(2023, 3).examples[0].input_data.split('\n')

def get_adjacent_indices(x, y, scheme):
    adj = [[0,1], [1,0], [0,-1], [-1,0], [1,1], [-1,-1], [1,-1], [-1,1]]
    return [(x+a[0], y+a[1]) for a in adj if len(scheme)>x+a[0]>=0 and len(scheme[0])>y+a[1]>=0]

def get_adjacent_gear_indices(x, span, scheme):
    adj_ind = set(list(chain.from_iterable(get_adjacent_indices(x, y, scheme) for y in range(span[0], span[1]))))

    return set([i for i in adj_ind if scheme[i[0]][i[1]]=='*'])

def get_adjacents(x, y, scheme):
    xys = get_adjacent_indices(x, y, scheme)
    #print(xys)
    return [scheme[xy[0]][xy[1]] for xy in xys]

def symbol_adjacent(x, span, scheme):
    surrounding = ''.join(list(chain.from_iterable([get_adjacents(x, y, puzzle) for y in range(span[0], span[1])])))


    return bool(re.search(r'[^\w,^.]', surrounding))

partsums = 0
parts_gears = {}
gears = []
parts = {}
for si in range(len(puzzle)):
    partsmatch = list(re.finditer(r'[\d]+', puzzle[si]))

    partsums += sum([int(p.group()) for p in partsmatch if symbol_adjacent(si, p.span(), puzzle)])

    for p in partsmatch:
        gear_ind = get_adjacent_gear_indices(si, p.span(), puzzle)
        if len(gear_ind)>0:
            parts_gears[(si, p.start())] = gear_ind
            parts[(si, p.start())] = int(p.group())

    gears.append([(si, g.start()) for g in list(re.finditer(r'\*', puzzle[si]))])

gears = list(chain.from_iterable(gears))

gear_ratio_sum = 0
for g in gears:
    gp = []
    for p in parts_gears:
        if g in parts_gears[p]:
            gp.append(parts[p])

    if len(gp) == 2:
        gear_ratio_sum += prod(gp)

print(f'Part 1: {partsums}')
print(f'Part 2: {gear_ratio_sum}')


