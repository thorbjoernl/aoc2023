from collections import defaultdict
from functools import cmp_to_key

CARDS = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]

def count_letters(string: str):
    result = defaultdict(lambda : 0)

    for c in string:
        result[c] = result[c] +1

    return result

def get_card_type(card):
    sorted_counts = sorted(card[2].values(), reverse=True)

    if sorted_counts[0] == 5:
        return 6
    if sorted_counts[0] == 4:
        return 5
    if sorted_counts[0] == 3:
        if sorted_counts[1] == 2:
            return 4
        else:
            return 3
    if sorted_counts[0] == 2:
        if sorted_counts[1] == 2:
            return 2
        else:
            return 1
    
    return 0

def compare_cards(c1, c2):
    if get_card_type(c1) - get_card_type(c2) != 0:
        return get_card_type(c1) - get_card_type(c2)
    
    for c1, c2 in zip(c1[0], c2[0]):
        if CARDS.index(c1) - CARDS.index(c2) != 0:
            return CARDS.index(c1) - CARDS.index(c2)

    return 0

def parse_configuration(file_name: str):
    with open(file_name, "r") as f:
        lines = f.readlines()

    hands = []
    for l in lines:
        split = l.split(" ")

        hands.append([split[0], int(split[1]), count_letters(split[0])])

    return hands

cards = parse_configuration("input.txt")

# Part 1
cards.sort(key = cmp_to_key(compare_cards))


points = 0
for i, c in enumerate(cards, start = 1):
    points = points + i*c[1]

print(f"Part 1 solution: {points}")