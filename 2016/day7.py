from aocd.models import Puzzle
import numpy as np
import re

puzzle = Puzzle(2016, 7)
raw = puzzle.input_data.split('\n')


def isABBA(s):
    for i in range(len(s) - 3):
        if s[i] == s[i + 3] and s[i + 1] == s[i + 2] and s[i] != s[i + 1]:
            return True

    return False


def getABA(s):
    abas = []
    for i in range(len(s) - 2):
        if s[i] == s[i + 2] and s[i] != s[i + 1]:
            abas += [(s[i], s[i + 1])]
            print(abas)

    return abas


def hasBABs(s, a, b):
    for i in range(len(s) - 2):
        if s[i] == b and s[i + 1] == a and s[i + 2] == b:
            return True

    return False


tls = 0
ssl = 0
for ip in raw:

    # find everything between brackets
    hypernet = re.findall(r'\[(.*?)\]', ip)

    # split all
    regular = re.split(r'\[(.*?)\]', ip)

    # remove strings between brackets
    [regular.remove(s) for s in hypernet]

    # check outside of brackets for any ABBA and make sure none in brackets
    if any([isABBA(s) for s in regular]) and not any(isABBA(s) for s in hypernet):
        tls += 1

    # check if any ABA
    abas = [getABA(s) for s in regular]
    abas = [pair for group in abas for pair in group]
    print(abas)
    ssl_found = False
    if any(abas):
        abas = [aba for aba in abas if len(aba) > 0]
        for a, b in abas:
            if any([hasBABs(s, a, b) for s in hypernet]) and not ssl_found:
                ssl_found = True

    if ssl_found:
        ssl += 1

print(f'Part 1: {tls}')
print(f'Part 2: {ssl}')
