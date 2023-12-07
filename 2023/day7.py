from aocd.models import Puzzle
from collections import Counter

puzzle = Puzzle(2023, 7)
data = puzzle.input_data.split('\n')

types = ['5', '14', '23', '113', '122', '1112', '11111']

def set_kinds(hands, wild_joker=False):
    for h in hands:
        c = Counter(h)

        if 'J' in c and h!= 'JJJJJ' and wild_joker:
            nJ = c.pop('J')
            c[c.most_common(1)[0][0]] += nJ

        kind = ''.join(sorted(list(str(n) for n in c.values())))
        hands[h]['type'] = kind

    return hands

def score(hands, J=11):
    cards = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
         '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10,
         'J': J, 'Q': 12, 'K': 13, 'A': 14}

    rank = 1
    winnings = 0
    for t in reversed(types):
        t_hands = [key for key, value in hands.items() if value['type'] == t]
        if t_hands:
            t_hands = sorted(t_hands, key=lambda x: [cards[c] for c in x])
        for h in t_hands:
            winnings += rank*hands[h]['bet']
            rank += 1

    return winnings

hands = {}
for h in data:
    hands[h.split()[0]] = {'bet': int(h.split()[1])}

print(f'Part 1: {score(set_kinds(hands))}')
print(f'Part 2: {score(set_kinds(hands, wild_joker=True), J=0)}')
