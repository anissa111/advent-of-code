from aocd.models import Puzzle


def part1(data):

    yardage = 0

    # for every package, calculate yardage and add to total
    for l in data:
        yardage += calc_yardage(l[0], l[1], l[2])

    return yardage


def part2(data):

    ribbon = 0

    # for every package, calculate ribbon length and add to total
    for l in data:
        ribbon += calc_ribbon(l[0], l[1], l[2])

    return ribbon


def calc_ribbon(x, y, z):

    # find perimeter of smallest side (presorted)
    ribbon = 2 * x + 2 * y

    # add volume for bow
    ribbon += x * y * z

    return ribbon


def calc_yardage(x, y, z):
    # find yardage and add length of smallest side
    return 2 * x * y + 2 * y * z + 2 * z * x + min([x * y, y * z, z * x])


def parse(raw):
    data = []

    # for every line, parse, sort, and add to data
    for l in raw.split('\n'):
        next = [int(x) for x in l.split('x')]
        next.sort()
        data.append(next)

    return data


if __name__ == '__main__':

    # import unique puzzle data
    puzzle = Puzzle(2015, 2)
    raw = puzzle.input_data

    data = parse(raw)

    answer1 = part1(data)
    answer2 = part2(data)

    print(f'Part 1: {answer1}')
    print(f'Part 2: {answer2}')
