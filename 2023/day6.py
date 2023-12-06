from aocd.models import Puzzle
import numpy as np
import re
from itertools import chain
from math import sqrt, floor, ceil
import matplotlib.pyplot as plt

puzzle = Puzzle(2023, 6)

data = puzzle.input_data.split('\n')
#data = puzzle.examples[0].input_data.split('\n')

# get pairs of t and d from input
tmax = [int(n) for n in re.findall(r'\d+', data[0])]
dmin = [int(n) for n in re.findall(r'\d+', data[1])]

# get the number of ways for each using quadratic eq and multiply together
nways=1
for t, d in zip(tmax, dmin):
    t1 = floor((t - sqrt(t*t - 4*d))/2)
    t2 = ceil((t + sqrt(t*t - 4*d))/2)
    nways *= t2-t1-1

print(f'Part 1 {nways}')

# squish all the numbers together
t = int(''.join(re.findall(r'\d+', data[0])))
d = int(''.join(re.findall(r'\d+', data[1])))

# another quadratic equation
t1 = floor((t - sqrt(t*t - 4*d))/2)
t2 = ceil((t + sqrt(t*t - 4*d))/2)
print(f'Part 1: {t2-t1-1}')