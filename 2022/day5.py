from aocd.models import Puzzle
import re
from pprint import pprint

def part1(s, directions):
    # progress state using directions
    for d in directions:
        # number of crates to move (times to pop and append)
        for i in range(d[0]):
            s[d[2]-1].append(s[d[1]-1].pop())

    # get top of each stack
    sf_top = [stack.pop() for stack in s]
    
    # convert to string and return
    return ''.join(sf_top)

def part2(s, directions):
    # progress state using directions
    for d in directions:
        # move crates
        s[d[2]-1].extend(s[d[1]-1][-(d[0]):])

        # delete crates from old position
        s[d[1]-1] = s[d[1]-1][:-(d[0])]

    # get top of each stack
    sf_top = [stack.pop() for stack in s]
    
    # convert to string and return
    return ''.join(sf_top)

def start_state(data):
    # split leaving blank strings 
    s0 = [re.split('    | ', l) for l in data]

    # reverse
    s0 = s0[::-1]

    # transpose 
    s0 = [[row[i] for row in s0] for i in range(len(s0[0]))]

    # remove blanks and brackets
    s0 = [[e[1] for e in l if e!=''] for l in s0]

    return s0

if __name__ == '__main__':
    puzzle = Puzzle(2022, 5)
    
    # convert string input to lists of ints
    data = puzzle.input_data.split('\n')

    # get initial state from first part of input
    s0 = start_state(data[0:8])

    # clean directions
    directions = [list(map(int, re.split('move | from | to | ', l)[1:])) for l in data[10::]]
    
    # run part 1
    answer1 = part1(s0.copy(), directions)

    # reset s0 since I can't for the life of me figure out how part1 is editing the original s0
    s0 = start_state(data[0:8])

    # run part 2
    answer2 = part2(s0, directions)

    print(f'Part 1: {answer1}')
    print(f'Part 2: {answer2}')
