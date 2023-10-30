from aocd.models import Puzzle
import numpy as np
from collections import defaultdict
import re

puzzle = Puzzle(2016, 13)
fav_number = int(puzzle.input_data)

def is_wall(xy, fav):
    x, y = xy
    code = x*x + 3*x + 2*x*y + y + y*y + fav

    if sum([int(x)for x in bin(code)[2:]]) % 2 == 0:
        return False

    return True

def print_office(x_range, y_range, fav):
    for y in range(y_range):
        print(''.join(['#' if is_wall((x, y), fav) else '.' for x in range(x_range)]))

def adjacent_empty(state, fav):
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    possible = []
    for d in dirs:
        loc = tuple(map(lambda i, j: i+j, state, d))
        if all([True if i >= 0 else False for i in loc]) and not is_wall(loc, fav):
            possible += [loc]
    return possible



def find_goal(start, fav, goal):
    history = set()
    possible_moves = {(start, 0)}
    while True:
        for _ in range(len(possible_moves)):
            curr_loc, step = possible_moves.pop()

            if curr_loc == goal:
                return step

            # new location
            if curr_loc not in history:
                history.add(curr_loc)
                possible_moves.update([(new_loc, step+1) for new_loc in adjacent_empty(curr_loc, fav)])

def find_max_loc(start, fav, steps):
    history = set()
    possible_moves = {(start, 0)}
    while len(possible_moves) > 0:
        for _ in range(len(possible_moves)):
            curr_loc, step = possible_moves.pop()

            # new location
            if curr_loc not in history and step+1 <= 50:
                possible_moves.update([(new_loc, step+1) for new_loc in adjacent_empty(curr_loc, fav)])

            history.add(curr_loc)

    return len(history)


#print_office(10,10, fav_number)
print(f'Part 1: {find_goal((1,1), fav_number, (31,39))}')
print(f'Part 2: {find_max_loc((1,1), fav_number, 50)}')