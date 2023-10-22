from aocd.models import Puzzle
import numpy as np

puzzle = Puzzle(2016, 9)
raw = puzzle.input_data


def format1(input):
    ptr = 0
    decomp_len = 0

    while ptr < len(input):
        if input[ptr] == '(':
            marker = input[ptr : input[ptr:].find(')') + 1 + ptr]
            data_len, rep = (int(n) for n in marker[1:-1].split('x'))

            # add to len and move pointer
            ptr += len(marker) + data_len
            decomp_len += data_len * rep
        elif input[ptr] == ' ':
            ptr += 1
        else:
            ptr += 1
            decomp_len += 1

    return decomp_len


def format2(input):
    ptr = 0
    decomp_len = 0

    if type(input) is int:
        print(input)

    while ptr < len(input):
        if input[ptr] == '(':
            marker = input[ptr : input[ptr:].find(')') + 1 + ptr]
            data_len, rep = (int(n) for n in marker[1:-1].split('x'))

            subset_len = format2(
                input[ptr + len(marker) : ptr + len(marker) + data_len]
            )

            # add to len and move pointer
            ptr += len(marker) + data_len
            decomp_len += subset_len * rep
        elif input[ptr] == ' ':
            ptr += 1
        else:
            ptr += 1
            decomp_len += 1

    return decomp_len


print(f'Part 1: {format1(raw)}')
print(f'Part 2: {format2(raw)}')
