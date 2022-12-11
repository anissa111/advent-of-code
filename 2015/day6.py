from aocd.models import Puzzle
import numpy as np


def part1(raw):

    # set up empty lights array
    lights = np.zeros((1000, 1000), dtype=int)

    # loop through instructions
    for l in raw.split("\n"):
        l = l.split()

        # if instruction is toggle
        if l[0] == "toggle":

            # get start and end coordinates
            start = [int(x) for x in l[1].split(",")]
            end = [int(x) for x in l[3].split(",")]

            # create a "sector" of lights
            sector = (slice(start[1], end[1] + 1), slice(start[0], end[0] + 1))

            # toggle lights in range
            lights[sector] = 1 - lights[sector]

        # if instruction is turn on or off
        else:

            # get start and end coordinates
            start = [int(x) for x in l[2].split(",")]
            end = [int(x) for x in l[4].split(",")]

            # create a "sector" of lights
            sector = (slice(start[1], end[1] + 1), slice(start[0], end[0] + 1))

            # if instruction is turn on
            if l[1] == "on":
                # set all lights between start and end to 1
                lights[sector] = 1
            # if instruction is turn off
            else:
                # set all lights between start and end to 0
                lights[sector] = 0

    # tally up the number of lights on
    return np.sum(lights)


def part2(raw):

    # set up empty lights array
    lights = np.zeros((1000, 1000), dtype=int)

    # loop through instructions
    for l in raw.split("\n"):
        l = l.split()

        # if instruction is toggle
        if l[0] == "toggle":

            # get start and end coordinates
            start = [int(x) for x in l[1].split(",")]
            end = [int(x) for x in l[3].split(",")]

            # create a "sector" of lights
            sector = (slice(start[1], end[1] + 1), slice(start[0], end[0] + 1))

            # increase brightness of lights in range by 2
            lights[sector] += 2

        # if instruction is turn on or off
        else:
            # get start and end coordinates
            start = [int(x) for x in l[2].split(",")]
            end = [int(x) for x in l[4].split(",")]

            # create a "sector" of lights
            sector = (slice(start[1], end[1] + 1), slice(start[0], end[0] + 1))

            # if instruction is turn on
            if l[1] == "on":
                # increase brightness by 1
                lights[sector] += 1
            # if instruction is turn off
            else:
                # decrease brightness by 1 to a minimum of 0
                lights[sector] = np.maximum(lights[sector] - 1, 0)

    #  tally up the light brightness
    return np.sum(lights)


if __name__ == "__main__":
    # import unique puzzle data
    puzzle = Puzzle(2015, 6)
    raw = puzzle.input_data

    answer1 = part1(raw)
    answer2 = part2(raw)

    print(f"Part 1: {answer1}")
    print(f"Part 2: {answer2}")
