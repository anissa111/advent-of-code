from aocd.models import Puzzle
from math import prod

puzzle = Puzzle(2022, 8)
data = puzzle.input_data.split('\n')
test_data = '''30373
25512
65332
33549
35390'''.split('\n')

# convert data to integer 2d
data = [[int(x) for x in l] for l in data]

# initialize visible to be the trees on the outside
# 2w + 2l - corners
visible = len(data)*2 + len(data[0])*2 - 4

# initialize scenic
scenic = []

# loop through interior trees
for i in range(len(data[0]))[1:-1]:
    for j in range(len(data))[1:-1]:
        # pull out tree for ease of access
        tree = data[i][j]

        # re-initialize scenic view score to empty
        view = []

        # make lists of compass directions surrounding tree
        # [left, right, up, down]
        w = data[i][0:j]; w.reverse()
        e = data[i][j+1:]
        n = [row[j] for row in data][0:i]; n.reverse()
        s = [row[j] for row in data][i+1:]
        directions = [w, e, n, s]

        # check to see if tallest in any direction
        if any([all(tree > ti for ti in direction) for direction in directions]):
            visible += 1
        
        # most scenic cannot be on border because x0
        for d in directions:
            for k in range(len(d)):
                if d[k] >= tree:
                    break
            view.append(k+1)
        scenic.append(prod(view))


print(f'Part 1: {visible}')
print(f'Part 2: {max(scenic)}')
