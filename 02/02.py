import re
from collections import defaultdict

id_pattern = r"\d+"

with open("input.txt", "r") as f:
    lines = f.readlines()

COLORS = ["red", "green", "blue"]

# Parsing data
games = []
for l in lines:
    game = {}
    segments = l.split(":")
    
    game["id"] = int(re.findall(id_pattern, segments[0])[0])

    # List to store separate "draws" within the game. Each draw is a dictionary
    # indexing amount by color as a string.
    game["draws"] = []
    
    for subset in segments[1].split(";"):
        new_draw = defaultdict(lambda : 0)

        for draw in subset.split(","):
            split = list(filter(None, draw.split(" ")))

            new_draw[split[1].strip()] = int(split[0].strip())
        
        game["draws"].append(new_draw)

    games.append(game)

# Solving part 1
_sum = 0

for g in games:
    allowed = True
    for d in g["draws"]:
        if d["red"] > 12:
            allowed = False
            break
        if d["green"] > 13:
            allowed = False
            break
        if d["blue"] > 14:
            allowed = False
            break
    
    if allowed:
        _sum = _sum + g["id"]

print(f"Part 1 - Solution: {_sum}")

_sum = 0

# Solving part 2
for g in games:
    min_red = max([x["red"] for x in g["draws"]])
    min_blue = max([x["blue"] for x in g["draws"]])
    min_green = max([x["green"] for x in g["draws"]])

    _sum = _sum + (min_red * min_blue * min_green)

print(f"Part 2 - Solution: {_sum}")
