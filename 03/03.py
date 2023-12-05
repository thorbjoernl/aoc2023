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
                        #print("Coord: ", a, b)
                        neighbours.append(lines[b][a])

        # Loop through neighbouring "tiles" and check if it is a symbol.
        has_symbol_neighbour = False
        for c in neighbours:
            if c in SYMBOLS:
                has_symbol_neighbour = True
                break
        
        # Append to list if symbol in neighbour "tile".
        if has_symbol_neighbour:
            numbers.append(int(string))

print(numbers)
print(sum(numbers))

# Solve Part 2.
