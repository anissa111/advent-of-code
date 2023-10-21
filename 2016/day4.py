from aocd.models import Puzzle
import numpy as np
from collections import Counter

# get puzzle data
puzzle = Puzzle(2016, 4)
raw = puzzle.input_data.split("\n")

# test input
# raw = ['aaaaa-bbb-z-y-x-123[abxyz]',
# 'a-b-c-d-e-f-g-h-987[abcde]',
# 'not-a-real-room-404[oarel]',
# 'totally-real-room-200[decoy]']

sectorIDsum = 0
realrooms = []
for room in raw:
    sectorID = int(room.split("-")[-1].split("[")[0])
    checksum = room.split("-")[-1].split("[")[1].split("]")[0]
    name = "".join(room.split("-")[:-1])

    counter = Counter(name)
    counts = dict(counter.most_common())

    check = ""
    while len(check) < 5:
        maximum = max(counts.values())
        tied = sorted([k for k, v in counts.items() if v == maximum])
        check += "".join(tied)
        [counts.pop(k) for k in tied]

    if check[:5] == checksum:
        sectorIDsum += sectorID
        realrooms.append([name, sectorID])

print(f"Part 1: {sectorIDsum}")

# decrypt real rooms
start = ord("a")
found = False
while not found:
    for name, sectorID in realrooms:
        shift = sectorID % 26

        decoded = "".join([chr(((ord(c) - start) + shift) % 26 + start) for c in name])
        if "northpole" in decoded:
            print(f"Part 2: {sectorID}")
            found = True
