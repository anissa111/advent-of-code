from aocd.models import Puzzle
import re

puzzle = Puzzle(2023, 10)
data = puzzle.input_data
#data = '.....\n.S-7.\n.|.|.\n.L-J.\n.....'

def get_possible(loc, data):
    dirs = [(0,1), (1,0), (0,-1),( -1,0)]
    possible = ['█┐-┘', '█┘|└', '█└-┌', '█┐|┌']
    inpossible = ['█-└┌', '█┐|┌', '█┐-┘', '█┘|└']
    valid = []
    for d, p, ip in zip(dirs, possible, inpossible):
        x = loc[0]+d[0]
        y = loc[1]+d[1]

        if x >= 0 and y >= 0 and x < len(data) and y < len(data[0]):
            if data[x][y] in p and data[loc[0]][loc[1]] in ip:
                valid.append((x, y))

    return valid


visual_pipes = {'L': '└', 'J': '┘', '7': '┐', 'F': '┌', 'S': '█'}

for p in visual_pipes:
    data = data.replace(p, visual_pipes[p])

data = [[c for c in d] for d in data.split('\n')]

start = [(index, row.index('█')) for index, row in enumerate(data) if '█' in row][0]

l = start
hist = [l]
steps = 0
while True:
    if steps > 1 and start in hist:
        hist.remove(start)

    l = list(set(get_possible(l, data)) - set(hist))[0]
    hist.append(tuple(l))
    steps += 1

    if data[l[0]][l[1]] == '█':
        break

print(f'Part 1: {steps//2}')
enclosed = 0
for ri in range(len(data)):
    inside = False
    for ci in range(len(data[0])):
        if (ri, ci) in hist:
            if data[ri][ci] in '|└┘':
                inside = not inside
        if inside and not (ri, ci) in hist:
            enclosed +=1

print(f'Part 2: {enclosed}')
