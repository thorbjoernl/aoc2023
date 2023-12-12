from functools import cache
def load_configuration(file_path):
    with open(file_path, "r") as f:
        lines = [l.strip() for l in f.readlines()]

        lines2 = [l.split(" ") for l in lines]

        lines3 = []
        for l in lines2:
            lines3.append((l[0], tuple(int(j) for j in l[1].split(","))))

        return lines3

def check_constraints(puzzle, constraint):
    partial_check = False
    counts = []
    current_count = 0
    for _, c in enumerate(puzzle):
        if c == "?":
            partial_check = True
            break
        elif c == "#":
            current_count = current_count +1
        elif c == ".":
            if current_count > 0:
                counts.append(current_count)
                current_count = 0
    
    if not partial_check and current_count > 0:
        counts.append(current_count)

    if partial_check:
        return all([count1 == count2 for count1, count2 in zip(counts, constraint[:len(counts)])])
    else:
        return (len(counts) == len(constraint)) and all([count1 == count2 for count1, count2 in zip(counts, constraint)])


def recursive_solver(puzzle, constraint):
    result = []

    # Find position of first "?"
    i = 0
    while i < len(puzzle):
        if puzzle[i] == "?":
            break
        i=i+1 
    
    if i >= len(puzzle):
        # No more question marks, return answer.
        if check_constraints(puzzle, constraint):
            #print(f"Puzzle {puzzle} succeeded constraint check, {constraint}")
            result.append(puzzle)
        #else:
            #print(f"Puzzle {puzzle} failed constraint check, {constraint}")
    else:
        new_puzzle = puzzle[:i] + "#" + puzzle[i + 1:]
        if check_constraints(new_puzzle, constraint):
            result.extend(recursive_solver(new_puzzle, constraint))

        new_puzzle = puzzle[:i] + "." + puzzle[i + 1:]
        if check_constraints(new_puzzle, constraint):
            result.extend(recursive_solver(new_puzzle, constraint))

    return result
            

data = load_configuration("input.txt")
#print(data)

# Part 1
_sum = 0
for d in data:
    print(f"{d}")
    _sum = _sum + len(recursive_solver(d[0], d[1]))

print(f"Solution Part 1: {_sum}")
# Solution: 8075
# 27,601.80 msec

#for d in data:
#    print(f"{d}")
#    _sum = _sum + len(recursive_solver(d[0], d[1]))**5
#
#print(f"Solution Part 2: {_sum}")

#_sum = 0
#for d in data:
#    print(d)
#    puzzle = d[0]
#    for _ in range(4):
#        puzzle = puzzle + "?" + d[0]

#    constraint = 5*d[1]

#    _sum = _sum + len(recursive_solver(puzzle, constraint))

#print(f"Solution Part 2: {_sum}")
