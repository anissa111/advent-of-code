import numpy as np
from aocd.models import Puzzle


def clean_input(raw):
    # get first row of input and separate by commas
    moves = raw.split()[0].split(",")

    # convert list of strings to list of ints
    moves = list(map(int, moves))

    # save back split without first moves row
    raw = raw.split()[1:]

    # get number of boards in input
    size = 5
    nboards = int(len(raw) / (size**2))  # will be 100

    # set up empty array for parsed boards
    boards = np.empty(shape=(nboards, size, size))
    for i in range(nboards):
        # parse next set of numbers into a 5x5
        board = np.reshape(raw[i * size**2 : i * size**2 + size**2], (size, size))

        # store parsed board
        boards[i] = board

    return moves, boards


def part1(moves, boards):
    # cycle through moves for all boards,
    # starting with first 5 moves for minimum success case
    for i in range(len(moves))[4:]:

        # check boards with moves so far to see if there is a winning board
        winboard, windex = findWin(moves[:i], boards)

        # if found, stop trying with additional moves
        if winboard is not None:
            # save current move added
            winarg = i

            break

    # calculate score of winning board
    score = scoreboard(winboard, moves, winarg)

    return score


def part2(moves, boards):
    # cycle through moves for all boards,
    # starting with first 5 moves for minimum success case

    for i in range(len(moves) + 1)[4:]:

        # check boards with moves so far to see if there is a winning board
        winboard, windex = findWin(moves[:i], boards)

        # find if multiple win boards for move
        while winboard is not None:

            # if found, remove it from boards list
            if winboard is not None:
                # save current move added
                winarg = i

                # remove board from boards list
                boards = np.delete(boards, windex, axis=0)

                lastwin = winboard
                lastwinarg = winarg

            # check boards with moves so far to see if there is another winning board
            winboard, windex = findWin(moves[:i], boards)

    # calculate score of last winning board:
    score = scoreboard(lastwin, moves, lastwinarg)

    return score


def scoreboard(winboard, moves, winarg):
    score = 0

    # find sum of unmarked numbers
    for element in winboard.flatten():
        if not np.isin(element, moves[:winarg]):
            score = score + element

    # multiply by last number called
    score = score * moves[winarg - 1]

    return score


def findWin(moves, boards):
    # check all boards
    index = 0
    for board in boards:
        iswin = checkwin(moves, board)

        if iswin:
            return board, index

        index = index + 1

    # if no win board return, return None
    return None, None


def checkwin(moves, board):
    # rows
    for row in board:
        mask = np.isin(row, moves)
        if all(mask):
            return True

    # columns
    for column in board.T:
        mask = np.isin(column, moves)
        if all(mask):
            return True

    # if no subset found, return False
    return False


if __name__ == "__main__":
    # import unique puzzle data
    puzzle = Puzzle(2021, 4)

    moves, boards = clean_input(puzzle.input_data)

    answer1 = part1(moves, boards)
    answer2 = part2(moves, boards)

    print(f"Part 1: {answer1}")
    print(f"Part 2: {answer2}")
