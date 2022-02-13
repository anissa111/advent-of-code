from aocd.models import Puzzle

def travel(data):
    # start at origin
    x = 0
    y = 0

    # define a set of houses
    houses = ({x,y})

    # go through each direction
    for d in data:
        if d == '^':
            y += 1
        elif d == 'v':
            y -= 1
        elif d == '>':
            x += 1
        elif d == '<':
            x -= 1
        
        # add the new house to the set
        houses.add((x,y))
    
    return houses

def part1(data):
    # check the length of the set of houses
    return len(travel(data))

def part2(data):

    # split data into santa and robot santa directions
    santa = data[0::2]
    robot_santa = data[1::2]

    # get the set of houses for each
    santa_houses = travel(santa)
    robot_santa_houses = travel(robot_santa)

    # return the length of the union of the two sets
    return len(santa_houses.union(robot_santa_houses)) - 1

if __name__ == '__main__':

    # import unique puzzle data
    puzzle = Puzzle(2015, 3)
    raw = puzzle.input_data

    answer1 = part1(raw)
    answer2 = part2(raw)

    print(f'Part 1: {answer1}')
    print(f'Part 2: {answer2}')
