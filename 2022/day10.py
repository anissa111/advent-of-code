from aocd.models import Puzzle

puzzle = Puzzle(2022, 10)
data = puzzle.input_data.split('\n')

register = [1]

for inst in data:
    register.append(register[-1])
    if inst != 'noop':
        register.append(register[-1] + int(inst.split(' ')[1]))

# print(register)
cycles = [20, 60, 100, 140, 180, 220]
sss = sum([register[i - 1] * i for i in cycles])
print(f'Part 1: {sss}')

l = 40
for i, x in enumerate(register):
    # print out # or . without newline
    print('#' if abs(x - (i % l)) <= 1 else '.', end='')

    # if end of length, new line
    if (i + 1) % l == 0:
        print()
