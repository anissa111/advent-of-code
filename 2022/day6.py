from aocd.models import Puzzle


def detect_unique(data, marker_size):

    # loop through groups of marker size
    for i in range(len(data) - marker_size + 1):
        marker = data[i : i + marker_size]
        if len(set(marker)) == marker_size:
            return i + marker_size


if __name__ == '__main__':
    puzzle = Puzzle(2022, 6)

    # get string
    data = puzzle.input_data.split()[0]

    # run part 1
    answer1 = detect_unique(data, 4)

    # run part 2
    answer2 = detect_unique(data, 14)

    print(f'Part 1: {answer1}')
    print(f'Part 2: {answer2}')
