from aocd.models import Puzzle
import numpy as np
import re

puzzle = Puzzle(2023,2).input_data.split('\n')
#puzzle = Puzzle(2023,2).examples[0].input_data.split('\n')

rmax = 12
gmax = 13
bmax = 14

possible_sum = 0
power_sum = 0

for gn in range(len(puzzle)):
    matches = puzzle[gn].split(':')[1].split(';')
    possible = True
    grmax = 0
    ggmax = 0
    gbmax = 0

    for m in matches:
        cubes = m.split(',')
        for c in cubes:
            match re.split(r' ', c)[1:]:
                case [n, 'blue']:
                    if int(n)>bmax: possible=False
                    if int(n)>gbmax: gbmax=int(n)
                case [n, 'green']:
                    if int(n)>gmax: possible=False
                    if int(n)>ggmax: ggmax=int(n)
                case [n, 'red']:
                    if int(n)>rmax: possible=False
                    if int(n)>grmax: grmax=int(n)

    power_sum += grmax*ggmax*gbmax

    if possible: possible_sum += gn + 1

print(f'Part 1: {possible_sum}')
print(f'Part 2: {power_sum}')

