from re import sub
from aocd.models import Puzzle

def part1(data):

    nice = 0

    # check each string for naughtiness
    for s in data.split('\n'):
        if three_vowels(s) and double_letter(s) and no_naughty(s):
            nice += 1
    
    return nice

def part2(data):

    nice = 0

    # check each string for naughtiness
    for s in data.split('\n'):
        if pairs(s) and one_between(s):
            nice += 1
    
    return nice

def pairs(s):

    substrings = []

    # check for pairs, check next for overlap
    for i, j, k in zip(s, s[1:], s[2:]):
        substrings.append([i,j])
        if i == j and j == k:
            # overlap occured, return false
            return False
    
    # check end of string
    substrings.append([s[-2],s[-1]])
    if s[-1] == s[-2] and s[-2] == s[-3]:
            return False  

    # check substrings for duplicates
    for i in substrings:
        if substrings.count(i) > 1:
            return True
    
    return False

def one_between(s):

    for i in range(len(s)-2):
        if s[i] == s[i+2]:
            return True
    
    return False


def three_vowels(s):
    vowels = {'a','e','i','o','u'}
    total = sum([s.count(v) for v in vowels])

    if total >= 3:
        return True
    
    return False
    

def double_letter(s):
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return True

    return False

def no_naughty(s):
    naughty = {'ab', 'cd', 'pq', 'xy'}
    for n in naughty:
        if n in s:
            return False
    
    return True

if __name__ == '__main__':
    # import unique puzzle data
    puzzle = Puzzle(2015, 5)
    raw = puzzle.input_data

    answer1 = part1(raw)
    answer2 = part2(raw)

    print(f'Part 1: {answer1}')
    print(f'Part 2: {answer2}')
