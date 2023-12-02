from aocd.models import Puzzle
import numpy as np
import re
from math import prod

puzzle = Puzzle(2023,2).input_data.split('\n')
#puzzle = Puzzle(2023,2).examples[0].input_data.split('\n')

totalmax = {'red': 12, 'green': 13, 'blue': 14,}

possible_sum = 0
power_sum = 0

for gn in range(len(puzzle)):

    counts = [list(map(int, re.findall(rf'(\d+) {color}', puzzle[gn]))) for color in totalmax]
    max_counts = [max(c) for c in counts]
    power_sum += prod(max_counts)

    if all([game<=total for game, total in zip(max_counts, list(totalmax.values()))]):
        possible_sum += gn + 1

print(f'Part 1: {possible_sum}')
print(f'Part 2: {power_sum}')

