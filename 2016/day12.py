from aocd.models import Puzzle
import numpy as np
from collections import defaultdict
import re

puzzle = Puzzle(2016, 12)
raw = puzzle.input_data.split('\n')

def run_instructions(instructions, registers):
    i = 0
    while i < len(instructions):
        match instructions[i].split(' '):
            case ['cpy', x, y]:
                if x.isdigit():
                    registers[y] = int(x)
                else:
                    registers[y] = registers[x]
                i += 1

            case ['inc', x]:
                registers[x] += 1
                i += 1

            case ['dec', x]:
                registers[x] -= 1
                i += 1

            case ['jnz', x, y]:
                if x.isdigit() and int(x) != 0:
                    i += int(y)
                elif not x.isdigit() and registers[x] != 0:
                    i += int(y)
                else:
                    i += 1
    return registers


print(f'Part 1: {run_instructions(raw, defaultdict(int))['a']}')

init_registers = defaultdict(int)
init_registers['c'] = 1
print(f'Part 2: {run_instructions(raw, init_registers)['a']}')