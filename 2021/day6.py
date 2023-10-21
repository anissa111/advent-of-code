import numpy as np
from aocd.models import Puzzle


def lifecycle(lf, days):

    pop = len(lf)

    spawn = np.zeros(days)

    # populate spawn
    for f in lf:
        spawn[f] = spawn[f] + 1

    # propagate initialized spawn
    for i in range(days)[:-7]:
        if i + 9 < days:
            spawn[i + 9] = spawn[i + 9] + spawn[i]
        spawn[i + 7] = spawn[i + 7] + spawn[i]

    # calculate total fish
    pop = pop + sum(spawn)

    return pop


if __name__ == '__main__':
    # import unique puzzle data
    puzzle = Puzzle(2021, 6)

    input = np.array(list((map(int, puzzle.input_data.split(',')))))

    test_input = np.array([3, 4, 3, 1, 2])

    answer1 = lifecycle(input, 80)
    answer2 = lifecycle(input, 256)

    print(f'Part 1: {answer1}')
    print(f'Part 2: {answer2}')
