from functools import cache

def load_input(file_path):
    with open(file_path, "r") as f:
        dat = [l.split(" ") for l in [m.strip() for m in f.readlines()]]

        return list(map(lambda d : (d[0], tuple(int(j) for j in d[1].split(","))), dat))

data = load_input("input.txt")

@cache
def n_arrangements(s, groups_left, size):
    """
    Counts the number of possible arrangements of a substring.
    s is the substring in question.
    groups_left is a tuple of the sizes of groups remaining.
    size is an integer indicating the size of the current spring
    group being considered.
    """
    if len(s) == 0:
        if len(groups_left) == 0 and size == 0:
            # Found solution is valid, count it.
            return 1
        elif len(groups_left) == 1 and size == groups_left[0]:
            # Found solution is valid, count it.
            return 1
        else:
            # Found combination is invalid.
            return 0

    if len(groups_left) > 0 and size > groups_left[0]:
        # A group in the middle was found that is to large given the remainig groups.
        return 0
    elif len(groups_left) == 0 and size > 0:
        # An additional group was found that is not compatible with the set of group sizes.
        return 0

    n = 0
    spring = s[0]

    if spring == "#" or spring == "?":
        n += n_arrangements(s[1:], groups_left, size +1)

    if spring == "." or spring == "?":
        if len(groups_left) > 0 and size == groups_left[0]:
            n+= n_arrangements(s[1:], groups_left[1:], 0)
        elif size == 0:
            n+= n_arrangements(s[1:], groups_left, 0)

    return n

def part_1():
    return sum(map(lambda d : n_arrangements(d[0], d[1], 0), data))
    
def part_2():
    return sum(map(lambda d : n_arrangements(d[0] + 4*("?" + d[0]), 5*d[1], 0), data))

print(f"Part 1: {part_1()}") # 8075
print(f"Part 2: {part_2()}") # 4232520187524
