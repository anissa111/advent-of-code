from aocd.models import Puzzle

puzzle = Puzzle(2022, 13)
data = puzzle.input_data.split('\n\n')

# parse data into nested int lists in groups of two
data = [[eval(line) for line in pair.split('\n')] for pair in data]

# write function to determine if a is 'smaller' than b
def compare(a, b):

    # if both ints
    if isinstance(a, int) and isinstance(b, int):
        return None if a == b else a < b

    # if one int, make sure both stay lists for compare
    elif isinstance(a, int):
        return compare([a], b)
    elif isinstance(b, int):
        return compare(a, [b])

    # if both exist, but neither int
    elif a and b:
        if (q := compare(a[0], b[0])) is not None:
            return q
        elif a[1:] or b[1:]:
            return compare(a[1:], b[1:])

    # if we're here, we've run out of one of them
    else:
        return None if len(a) == len(b) else len(b) > len(a)


# find sum of packet pair indices that are in order
ans1 = sum([i + 1 if compare(data[i][0], data[i][1]) else 0 for i in range(len(data))])
print(f'Part 1: {ans1}')

# restructure data to remove pairs grouping
data = [packet for pair in data for packet in pair]

# find how many packets come before [[2]] and [[6]] (which will include [[2]])
ans2 = (sum([0 if compare([[2]], data[i]) else 1 for i in range(len(data))])) + 1
ans2 *= (sum([0 if compare([[6]], data[i]) else 1 for i in range(len(data))])) + 2
print(f'Part 2: {ans2}')
