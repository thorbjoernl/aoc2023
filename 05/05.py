
with open("example.txt", "r") as f:
    lines = f.readlines()


seeds = [x for x in map(lambda x : int(x.strip()), list(filter(None, lines[0].split(":")[1].split(" "))))]


for i, l in enumerate(lines):
    if l == "seed-to-soil map:\n":
        break

lines = lines[i+1:]

for i, l in enumerate(lines):
    if l == "soil-to-fertilizer map:\n":
        break
    
print(lines)