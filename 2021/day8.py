import numpy as np
from aocd.models import Puzzle


def parse(raw):

    input = [
        tuple(map(lambda raw: raw.split(), l.split(" | "))) for l in raw.split("\n")
    ]

    return input


def decode(line):

    decoded = np.zeros(len(line), dtype=int)

    for i in range(len(line)):
        n = line[i]

        if len(n) == 2:
            decoded[i] = 1

        elif len(n) == 4:
            decoded[i] = 4

        elif len(n) == 3:
            decoded[i] = 7

        elif len(n) == 7:
            decoded[i] = 8

        elif "f" not in n:
            decoded[i] = 0

        elif "a" not in n and "g" not in n:
            decoded[i] = 5

        elif "e" not in n and "b" not in n:
            decoded[i] = 2

        elif "e" not in n and "g" not in n:
            decoded[i] = 3

        elif "a" not in n:
            decoded[i] = 6

        elif "g" not in n:
            decoded[i] = 9

    return decoded


def part1(input):

    uniques = 0

    for l in input:
        digits = decode(l[1]).tolist()

        uniques = (
            uniques
            + digits.count(1)
            + digits.count(4)
            + digits.count(7)
            + digits.count(8)
        )

    return uniques


def part2(input):

    print(input)

    sum = 0
    for l in input:

        sum = sum + int("".join(map(str, decode(l[1]).tolist())))

    return sum


if __name__ == "__main__":
    # import unique puzzle data
    puzzle = Puzzle(2021, 8)

    # parse input string into list of ints
    raw = puzzle.input_data

    test_raw = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"""

    test_input = parse(test_raw)
    input = parse(raw)

    answer1 = part1(test_input)
    answer2 = part2(test_input)
    #
    print(f"Part 1: {answer1}")
    print(f"Part 2: {answer2}")
