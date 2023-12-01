from aocd.models import Puzzle
import re

puzzle = Puzzle(2016, 15).input_data.split('\n')
#puzzle = ['Disc #1 has 5 positions; at time=0, it is at position 4.','Disc #2 has 2 positions; at time=0, it is at position 1.']
puzzle.append('Disc #7 has 11 positions; at time=0, it is at position 0.')

n_disks = len(puzzle)
positions = []
slots = []
for l in puzzle:
    positions.append(int(re.findall(r'\d+', l)[-1]))
    slots.append(int(re.findall(r'\d+', l)[1]))

out_order = [0]*n_disks
for di in range(n_disks):
    out_order[di] = slots[di]- 1 - di

time_step = max(slots)-1
time_start = 0
if time_start < 0:
    time_start += slots[slots.index(max(slots))]
t = time_start
while True:
    pt = [(positions[i] + t) % slots[i] for i in range(n_disks)]

    if pt == out_order:
        break

    t += 1

#print(f'Part 1: {t}')
print(f'Part 2: {t}')
