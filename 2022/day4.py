from aocd.models import Puzzle
import re

def part1(data):
    encompassed = 0
    for pair in data:
        # find smaller section
        if pair[1] - pair[0] <= pair[3] - pair[2]:
            # first smaller or equal
            if pair[0] >= pair[2] and pair[1] <= pair[3]:
                encompassed += 1
        else:
            # second smaller
            if pair[0] <= pair[2] and pair[1] >= pair[3]:
                encompassed += 1

    return encompassed

def part2(data):
    # find sections that /don't/ overlap and subtract from total
    total_sections = len(data)   # 1000
    no_touch = 0

    for pair in data:
        if (pair[1] < pair[2] and pair[0] < pair[2]) or (pair[3] < pair[0] and pair[2] < pair[0]):
            no_touch += 1
    
    return total_sections - no_touch


def clean_ranges(data):
    return [list(map(int, re.split('-|,', d))) for d in data]

if __name__ == '__main__':
    puzzle = Puzzle(2022, 4)
    
    # convert string input to lists of ints
    data = puzzle.input_data.split('\n')
    
    # clean and convert to integers
    clean_data = clean_ranges(data)

    # run part 1
    answer1 = part1(clean_data)

    # run part 2
    answer2 = part2(clean_data)

    print(f'Part 1: {answer1}')
    print(f'Part 2: {answer2}')
