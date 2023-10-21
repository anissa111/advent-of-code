from aocd.models import Puzzle
from pprint import pprint
from collections import defaultdict

puzzle = Puzzle(2022, 7)

# get string commands
data = puzzle.input_data.split('\n')

dirs = defaultdict(int)
dirs['/'] = 0
pwd = ['/']

# ignore first 'cd /' command
data.pop(0)

for cmd in data:
    cmd = cmd.split(' ')

    # handle cd commands
    if cmd[1] == 'cd':
        # if move up
        if cmd[2] == '..':
            pwd.pop()
        # move down
        else:
            # i know this doesn't exactly look right, but it does its purpose
            pwd.append(''.join(pwd) + cmd[2] + '/')

    # if size
    elif cmd[0].isdigit():
        for d in pwd:
            dirs[d] += int(cmd[0])

total_space = 70_000_000
needed_space = 30_000_000
unused_space = total_space - dirs['/']

print(f'Part 1: {sum(v for v in dirs.values() if v <= 100_000)}')
print(f'Part 2: {min(v for v in dirs.values() if (v+unused_space)>=needed_space)}')
