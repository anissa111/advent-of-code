from aocd.models import Puzzle
import numpy as np
from collections import Counter

# get puzzle data
puzzle = Puzzle(2016, 6)
raw = np.array(puzzle.input_data.split('\n'))

raw = np.array([list(l) for l in raw]).T

message1 = ''
message2 = ''
for row in raw:
    counts = dict(Counter(row))
    message1 += max(counts, key=counts.get)
    message2 += min(counts, key=counts.get)

print(f'Part 1: {message1}')
print(f'Part 2: {message2}')