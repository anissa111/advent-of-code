from aocd.models import Puzzle

def part1(data):
    priority_sum = 0
    for d in data:
        whoops = ''.join(set(d[0:len(d)//2:]).intersection(set(d[len(d)//2::])))
        priority_sum += ord(whoops) - 96 if whoops.islower() else ord(whoops) - 64 + 26

    return priority_sum

def part2(data):
    priority_sum = 0
    for e1, e2, e3 in zip(data[0::3], data[1::3], data[2::3]):
        badge = ''.join(set(e1).intersection(e2).intersection(e3))
        priority_sum += ord(badge) - 96 if badge.islower() else ord(badge) - 64 + 26
    
    return priority_sum

if __name__ == '__main__':
    puzzle = Puzzle(2022, 3)
    
    # convert string input to lists of ints
    data = puzzle.input_data.split('\n')

    # run part 1
    answer1 = part1(data)

    # run part 2
    answer2 = part2(data)

    print(f'Part 1: {answer1}')
    print(f'Part 2: {answer2}')
