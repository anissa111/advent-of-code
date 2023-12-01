from aocd.models import Puzzle

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

overlaps = {
    'oneight': 'oneeight',
    'threeignt': 'threeeight',
    'fiveignt': 'fiveeight',
    'nineight': 'nineeight',
    'twone': 'twoone',
    'sevenine': 'sevennine',
    'eightwo': 'eighttwo',
}

calibration_sum_1 = 0
calibration_sum_2 = 0

for l in puzzle:
    l_1 = [d for d in l if d.isdigit()]
    calibration_sum_1 += int(''.join([l_1[0], l_1[-1]]))

    for o in overlaps:
        l = l.replace(o, overlaps[o])
    for n in str_nums:
        l = l.replace(n, str_nums[n])
    l_2 = [d for d in l if d.isdigit()]
    calibration_sum_2 += int(''.join([l_2[0], l_2[-1]]))


print(f'Part 1: {calibration_sum_1}')
print(f'Part 2: {calibration_sum_2}')
