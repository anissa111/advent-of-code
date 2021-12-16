from aocd.models import Puzzle


def part1(data):
    deeper = 0
    for a, b in zip(data[:-1], data[1:]):
        if b > a:
            deeper = deeper + 1

    return deeper


def part2(data):
    deeper = 0
    for a1, a2b1, a3b2, b3 in zip(data[:-3], data[1:-2], data[2:-1], data[3:]):
        if sum([a2b1, a3b2, b3]) > sum([a1, a2b1, a3b2]):
            deeper = deeper + 1

    return deeper


if __name__ == '__main__':
    # import unique puzzle data
    puzzle = Puzzle(2021, 1)

    # convert string input to list of ints
    clean_data = list(map(int, puzzle.input_data.split('\n')))

    # run part 1
    answer1 = part1(clean_data)

    # run part 2
    answer2 = part2(clean_data)

    print(f'Part 1: {answer1}')
    print(f'Part 2: {answer2}')
