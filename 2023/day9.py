from aocd.models import Puzzle
from numpy.polynomial.polynomial import Polynomial

puzzle = Puzzle(2023, 9)
data = puzzle.input_data.split('\n')
#ata = puzzle.examples[0].input_data.split('\n')

data = [[int(i) for i in d.split()] for d in data]

next_sum = 0
prev_sum = 0
for l in data:
    p = Polynomial.fit(list(range(len(l))), l, len(l)-1)
    next_sum += round(p(len(l)))
    prev_sum += round(p(-1))

print(f'Part 1: {next_sum}')
print(f'Part 2: {prev_sum}')
