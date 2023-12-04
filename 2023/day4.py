from aocd.models import Puzzle
import numpy as np
import re
from math import pow

puzzle = Puzzle(2023, 4).input_data.split('\n')
#puzzle = Puzzle(2023, 4).examples[0].input_data.split('\n')

pts = 0
originals = {}
for ci in range(len(puzzle)):
    c = puzzle[ci].split(':')[1]
    win, have = (set(re.findall(r'\d+', x)) for x in c.split('|'))

    n_win = len(win.intersection(have))
    pts += int(pow(2, n_win-1))

    # collect a dict of how many points each card has for pt 2
    originals[ci+1] = n_win

print(f'Part 1: {pts}')

card_queue = list(originals)
total = len(originals)

while True:
    c = card_queue.pop()

    # if a card has wins, add the next n=wins cards to the queue and update total
    if originals[c] > 0:
        mults = list(range(c+1, min(c+originals[c]+1, len(originals)))) # make sure not to add a card # > possible cards

        card_queue += mults
        total += len(mults)

    # break if no more cards to go through
    if len(card_queue) < 1:
        break

print(f'Part 2: {total}')
