from aocd.models import Puzzle
import numpy as np
from collections import defaultdict
import re

puzzle = Puzzle(2016, 10)
raw = puzzle.input_data.split('\n')

bots = defaultdict(list)
botinstr = defaultdict(list)
for instr in raw:
    match re.split(r'(\d+)', instr)[:-1]:
        case ['value ', val, ' goes to bot ', botnum]:
            bots[int(botnum)].append(int(val))
        case [
            'bot ',
            botnum,
            ' gives low to bot ',
            botlow,
            ' and high to bot ',
            bothigh,
        ]:
            botinstr[int(botnum)] = [int(botlow), int(bothigh)]


def find_compare(bots, botinstr):
    while True:
        readybots = [key for key in bots if len(bots[key]) > 1]
        for bot in readybots:
            low, high = sorted(bots[bot])
            if low == 17 and high == 61:
                return bot
            bots[botinstr[bot][0]].append(low)
            bots[botinstr[bot][1]].append(high)
            botinstr.pop(bot)
            bots.pop(bot)


part1 = find_compare(bots, botinstr)
print(f'Part 1: {part1}')
