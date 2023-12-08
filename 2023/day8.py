from aocd.models import Puzzle
from math import lcm

puzzle = Puzzle(2023, 8)

data = puzzle.input_data.split('\n')
directions = data[0]

network = {}
for d in data[2:]:
    network[d[0:3]] = {'L': d[7:10], 'R': d[12:15]}

loc = 'AAA'
steps = 0
while loc != 'ZZZ':
    for d in directions:
        steps +=1
        loc = network[loc][d]

print(f'Part 1: {steps}')

steps = 0
locs = [n for n in network if n[2] == 'A']
firstz = []

for l in locs:
    s = 0
    while l[2] != 'Z':
        for d in directions:
            s += 1
            l = network[l][d]

    firstz.append(s)

print(f'Part 2: {lcm(*firstz)}')