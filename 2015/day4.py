from aocd.models import Puzzle
from hashlib import md5


def find_hash(pref, key):
    key = key.encode("ascii")
    suffix = 1

    # loop until we find a hash that starts with the prefix
    while True:
        hash = md5(key + str(suffix).encode("ascii")).hexdigest()

        if hash.startswith(pref):
            return suffix

        suffix += 1


if __name__ == "__main__":

    # import unique puzzle data
    puzzle = Puzzle(2015, 4)
    secret_key = puzzle.input_data

    answer1 = find_hash("00000", secret_key)
    answer2 = find_hash("000000", secret_key)

    print(f"Part 1: {answer1}")
    print(f"Part 2: {answer2}")
