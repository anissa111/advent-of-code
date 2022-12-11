from aocd.models import Puzzle


def split_clean(data):
    p1 = [ord(m.lower()) - 96 for m in data[0::2]]
    p2 = [ord(m.lower()) - 96 - 23 for m in data[1::2]]

    return p1, p2


def score_1(m1, m2):
    shape_score = m2

    # win score
    tie = m1 == m2
    win = (m1 == 3 and m2 == 1) or (m1 == 2 and m2 == 3) or (m1 == 1 and m2 == 2)

    # lose
    win_score = 0
    # tie
    if tie:
        win_score = 3
    # win
    elif win:
        win_score = 6

    return win_score + shape_score


def score_2(m1, result):

    # calculate win score from result
    win_score = (result - 1) * 3

    # figure out which move to play
    # tie
    if result == 2:
        shape_score = m1
    # win
    elif result == 3:
        shape_score = (m1 % 3) + 1
    # lose
    else:
        shape_score = ((m1 + 1) % 3) + 1

    return win_score + shape_score


def tally(p1, p2, scorer):
    # tally scores for all moves
    scores = [scorer(m1, m2) for m1, m2 in zip(p1, p2)]
    return sum(scores)


if __name__ == "__main__":
    puzzle = Puzzle(2022, 2)

    # convert string input to lists of ints
    data = puzzle.input_data.split()

    p1, p2 = split_clean(data)

    # run part 1
    answer1 = tally(p1, p2, score_1)

    # run part 2
    answer2 = tally(p1, p2, score_2)

    print(f"Part 1: {answer1}")
    print(f"Part 2: {answer2}")
