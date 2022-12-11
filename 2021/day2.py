from aocd.models import Puzzle


def part1(input):
    x = 0
    y = 0

    for instruction in input:

        instruction = instruction.split()

        if instruction[0] == "forward":
            x = x + int(instruction[1])
        elif instruction[0] == "down":
            y = y + int(instruction[1])
        elif instruction[0] == "up":
            y = y - int(instruction[1])
        else:
            print("unexpected input")

    return x * y


def part2(input):
    x = 0
    y = 0
    aim = 0

    for instruction in input:

        instruction = instruction.split()

        if instruction[0] == "forward":
            x = x + int(instruction[1])
            y = y + int(instruction[1]) * aim
        elif instruction[0] == "down":
            aim = aim + int(instruction[1])
        elif instruction[0] == "up":
            aim = aim - int(instruction[1])
        else:
            print("unexpected input")

    return x * y


if __name__ == "__main__":
    # import unique puzzle data
    puzzle = Puzzle(2021, 2)

    # convert string input to list of ints
    raw = puzzle.input_data.split("\n")

    # run part 1
    answer1 = part1(raw)

    # run part 2
    answer2 = part2(raw)

    print(f"Part 1: {answer1}")
    print(f"Part 2: {answer2}")
