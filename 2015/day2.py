from aocd.models import Puzzle

def part1(data):

    yardage = 0

    # for every package, calculate yardage and add to total
    for l in data:
        yardage += calc_yardage(l[0],l[1],l[2])
    
    return yardage


def calc_yardage(x,y,z):
    # find yardage and add length of smallest side
    return 2*x*y + 2*y*z + 2*z*x + min([x*y,y*z,z*x])


def parse(raw):
    data = []
    for l in raw.split('\n'):
        data.append([int(x) for x in l.split('x')])
    
    return data


if __name__ == '__main__':

    # import unique puzzle data
    puzzle = Puzzle(2015, 2)
    raw = puzzle.input_data

    data = parse(raw)

    answer1 = part1(data)

    print(f'Part 1: {answer1}')