from aocd.models import Puzzle
import numpy as np
import re
from itertools import chain
from math import sqrt, floor, ceil
from collections import Counter

puzzle = Puzzle(2023, 7)

data = puzzle.input_data.split('\n')
#data = puzzle.examples[0].input_data.split('\n')

hands = {}
#types = {'5': 1, '14': 2, '23': 3, '113': 4, '122': 5, '1112': 6, '11111': 7}
types = ['5', '14', '23', '113', '122', '1112', '11111']
for h in data:
    c = Counter(h.split()[0])
    kind = ''.join(sorted(list(str(n) for n in c.values())))
    hands[h.split()[0]] = {'bet': int(h.split()[1]), 'type': kind}

cards = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
         '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10,
         'J': 11, 'Q': 12, 'K': 13, 'A': 14}
rank = 1
winnings = 0
for t in reversed(types):
    t_hands = [key for key, value in hands.items() if value['type'] == t]
    if t_hands:
        # sort by order of cards
        t_hands = sorted(t_hands, key=lambda x: [cards[c] for c in x])
    for h in t_hands:
        winnings += rank*hands[h]['bet']
        rank += 1

print(f'Part 1: {winnings}')


