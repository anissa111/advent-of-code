import numpy as np
from aocd.models import Puzzle


def lifecycle(lf, days):

    # print(f'After 0 days: {lf}')

    for i in range(days):

        # spawn new fish with an extra day
        lf = np.append(lf, np.ones(len(lf[lf == 0])) * 9)

        # decrease days for all fish
        lf = lf - 1

        # cycle fist that have completed spawn
        lf[lf == -1] = 6


        # print(f'After {i+1} days: {lf}')

    return len(lf)

def calc_children(lf, days)



if __name__ == '__main__':
    # import unique puzzle data
    puzzle = Puzzle(2021, 6)

    input = np.array(list((map(int, puzzle.input_data.split(',')))))
    days = 80

    test_input = np.array([3, 4, 3, 1, 2])

    answer1 = lifecycle(input, 80)
    answer2 = lifecycle(input, 256)

    print(f'Part 1: {answer1}')
    print(f'Part 2: {answer2}')
