from aocd.models import Puzzle
from math import dist, copysign

puzzle = Puzzle(2022, 9)
data = puzzle.input_data.split("\n")
data = [[r.split()[0], int(r.split()[1])] for r in data]
move_dict = {"U": [0, 1], "D": [0, -1], "L": [-1, 0], "R": [1, 0]}


def simulate(rope):
    tail_pos = [str([0, 0])]

    # loop through movements
    for m, n in data:
        # update in direction n times
        for _ in range(n):

            # update head
            rope[0] = [rope[0][0] + move_dict[m][0], rope[0][1] + move_dict[m][1]]

            # update rest
            for i in range(1, len(rope)):
                new_pos = move(rope[i].copy(), rope[i - 1].copy())
                rope[i] = new_pos

            # update where tail has been
            tail_pos.append(str(rope[-1]))

    return len(set(tail_pos))


# move knots based on leading knot position
def move(knot, lead):
    dx = lead[0] - knot[0]
    dy = lead[1] - knot[1]

    # if side by side or overlapping, do not move
    if abs(dx) <= 1 and abs(dy) <= 1:
        return knot

    if abs(dx) > 1 or (abs(dx) + abs(dy)) > 2:
        knot[0] += int(copysign(1, dx))

    if abs(dy) > 1 or (abs(dx) + abs(dy)) > 2:
        knot[1] += int(copysign(1, dy))

    return knot


print(f"Part 1: {simulate([[0,0]] * 2)}")
print(f"Part 2: {simulate([[0,0]] * 10)}")
