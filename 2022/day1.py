from aocd.models import Puzzle


def part1(data):
    # how many calories is the elf with the most calories holding?
    totals = [sum(sub_list) for sub_list in data]
    totals.sort(reverse=True)
    return totals[0]


def part2(data):
    # how many calories are the top 3 elves with the most calories holding?
    totals = [sum(sub_list) for sub_list in data]
    totals.sort(reverse=True)
    return sum(totals[:3])


if __name__ == '__main__':
    puzzle = Puzzle(2022, 1)

    # convert string input to lists of ints
    clean_data = []
    elf = []
    for l in puzzle.input_data.split('\n'):
        if l != '':
            elf.append(int(l))
        else:
            clean_data.append(elf)
            elf = []

    # run part 1
    answer1 = part1(clean_data)

    # run part 2
    answer2 = part2(clean_data)

    print(f'Part 1: {answer1}')
    print(f'Part 2: {answer2}')
