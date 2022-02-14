from aocd.models import Puzzle

def score(n):
    return sum(int(x) for x in str(n))


if __name__ == '__main__':
    # import unique puzzle data
    puzzle = Puzzle(2021, 10)

    # parse input string into list of ints
    raw = puzzle.input_data

    test_raw = '''[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]'''

    test_input = parse(test_raw)
    input = parse(raw)

    answer1 = part1(input)
    # answer2 = part2(test_input)

    print(f'Part 1: {answer1}')
    # print(f'Part 2: {answer2}')