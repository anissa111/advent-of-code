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
        case ['bot ', botnum, ' gives low to bot ', botlow, ' and high to bot ', bothigh]:
            botinstr[int(botnum)]= ['bot-bot', int(botlow), int(bothigh)]
        case ['bot ', botnum, ' gives low to bot ', botlow, ' and high to output ', outhigh]:
            botinstr[int(botnum)]= ['bot-out', int(botlow), int(outhigh)]
        case ['bot ', botnum, ' gives low to output ', outlow, ' and high to bot ', bothigh]:
            botinstr[int(botnum)]= ['out-bot', int(outlow), int(bothigh)]
        case ['bot ', botnum, ' gives low to output ', outlow, ' and high to output ', outhigh]:
            botinstr[int(botnum)]= ['out-out', int(outlow), int(outhigh)]

def find_compare(bots, botinstr):
    while True:
        readybots = [key for key in bots if len(bots[key])>1]
        for bot in readybots:
            low, high = sorted(bots[bot])
            if low == 17 and high == 61:
                return bot
            bots[botinstr[bot][1]].append(low)
            bots[botinstr[bot][2]].append(high)
            botinstr.pop(bot)
            bots.pop(bot)

def find_outs(bots, botinstr):
    outs = defaultdict(list)
    while len(botinstr) > 0 and len(readybots:=[key for key in bots if len(bots[key])>1]) > 0:
        for bot in readybots:
            low, high = sorted(bots[bot])
            match botinstr[bot][0]:
                case 'bot-bot':
                    bots[botinstr[bot][1]].append(low)
                    bots[botinstr[bot][2]].append(high)
                case 'out-bot':
                    outs[botinstr[bot][1]].append(low)
                    bots[botinstr[bot][2]].append(high)
                case 'bot-out':
                    bots[botinstr[bot][1]].append(low)
                    outs[botinstr[bot][2]].append(high)
                case 'out-out':
                    outs[botinstr[bot][1]].append(low)
                    outs[botinstr[bot][2]].append(high)

            botinstr.pop(bot)
            bots.pop(bot)

    return outs

part1 = find_compare(bots, botinstr)
print(f'Part 1: {part1}')

outs = find_outs(bots, botinstr)
part2 = outs[0][0] * outs[1][0] * outs[2][0]
print(f'Part 2: {part2}')