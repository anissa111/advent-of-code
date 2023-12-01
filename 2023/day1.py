from aocd.models import Puzzle
import numpy as np

puzzle = Puzzle(2023,1).input_data.split('\n')

str_nums = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}

calibration_sum_1 = 0
calibration_sum_2 = 0
for l in puzzle:
    l_1 = [d for d in l if d.isdigit()]
    calibration_sum_1 += int(''.join([l_1[0], l_1[-1]]))

for l in puzzle:
    partial = ''
    first = None
    last = None

    partial = ''
    while first is None:
        for c in l:
            if c.isdigit() and first is None:
                first = c
            partial = partial + c
            str_check = [n in partial for n in str_nums]
            if any(str_check) and first is None:
                first = str(str_check.index(True)+1)

    while last is None:
        for c in l[::-1]:
            if c.isdigit() and last is None:
                last = c
            partial = c + partial
            str_check = [n in partial for n in str_nums]
            if any(str_check) and last is None:
                last = str(str_check.index(True)+1)





    calibration_sum_2 += int(''.join([first, last]))


print(f'Part 1: {calibration_sum_1}')
print(f'Part 2: {calibration_sum_2}')


