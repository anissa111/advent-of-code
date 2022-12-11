from math import floor, prod

# we're going to manually input this one
monkeys = [
    [54, 61, 97, 63, 74],
    [61, 70, 97, 64, 99, 83, 52, 87],
    [60, 67, 80, 65],
    [61, 70, 76, 69, 82, 56],
    [79, 98],
    [72, 79, 55],
    [63],
    [72, 51, 93, 63, 80, 86, 81],
]

inspected = [0] * len(monkeys)

divs = [17, 2, 5, 3, 7, 13, 19, 11]

ops = [
    lambda a: a * 7,
    lambda a: a + 8,
    lambda a: a * 13,
    lambda a: a + 7,
    lambda a: a + 2,
    lambda a: a + 1,
    lambda a: a + 4,
    lambda a: a * a,
]

true_cond = [5, 7, 1, 5, 0, 2, 7, 0]
false_cond = [3, 6, 6, 2, 3, 1, 4, 4]

# rounds = 20
rounds = 10_000


# simulate rounds
for _ in range(rounds):

    # go through each monkey
    for i, monkey in enumerate(monkeys):
        for _ in range(len(monkey)):
            # pull first item in array
            curr = monkey.pop(0)

            # add to inspection number
            inspected[i] += 1

            # do worry operation
            # curr = floor(ops[i](curr) / 3.0)
            curr = ops[i](curr)

            # mod
            mod = prod(divs)

            # check condition
            monkeys[true_cond[i]].append(curr % mod) if curr % divs[
                i
            ] == 0 else monkeys[false_cond[i]].append(curr % mod)

inspected.sort()
inspected.reverse()

print(f"Ans: {inspected[0] * inspected[1]}")
