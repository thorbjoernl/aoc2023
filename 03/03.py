import re

pattern_number = r"\d+"
SYMBOLS = ["*", "#", "+", "$", "=", "/", "-", "@", "%", "&"]

with open("input.txt", "r") as f:
    l = f.readlines()

# Trim whitespace.
lines = [x.strip() for x in l]

# Get dimensions
width = len(lines[0])
height = len(lines)

# Solve Part 1
numbers = []
for i, l in enumerate(lines):
    matches = re.finditer(pattern_number, l)

    for m in matches:
        string = m.group()
        x= m.start()
        y= i
        w=m.end()-m.start()

        # Generate list of neighbouring "tiles".
        # This list contains the tiles making up the number itself, but since the number is 
        # guaranteed to be symbol free it still works. Ignores tiles that are out of bounds.

        neighbours = []
        for a in range(x-1, x+w+1):
            for b in range(y-1, y+2):
                if a >= 0 and a < width:
                    if b>= 0 and b < height:
                        neighbours.append(lines[b][a])

        # Loop through neighbouring "tiles" and check if it is a symbol.
        if any([(c in SYMBOLS) for c in neighbours]):
            numbers.append(int(string))

print(f"Part 1 Solution: {sum(numbers)}")

# Solve Part 2.
