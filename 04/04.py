from collections import defaultdict

with open("input.txt", "r") as f:
    lines = f.readlines()


# Part 1
grand_sum = 0
for l in lines:
    substrings = l.split(":")[1].split("|")

    winning_numbers = set([x for x in map(lambda x : int(x.strip()), list(filter(None, substrings[0].split(" "))))])
    
    numbers = [x for x in map(lambda x : int(x.strip()), list(filter(None, substrings[1].split(" "))))]

    count = 0
    for n in numbers:
        if n in winning_numbers:
            count = count +1

    grand_sum = grand_sum + int(2**(count-1))

print(grand_sum)

# Part 2
cards = []

for i, l in enumerate(lines):
    substrings = l.split(":")[1].split("|")

    winning_numbers = set([x for x in map(lambda x : int(x.strip()), list(filter(None, substrings[0].split(" "))))])
    
    numbers = [x for x in map(lambda x : int(x.strip()), list(filter(None, substrings[1].split(" "))))]

    cards.append(
        {
            "id": i,
            "winners": winning_numbers,
            "numbers": numbers
        }
    )

data = defaultdict(lambda : 0)
for c in cards:
    # Add 1 for the original.
    data[c["id"]] = data[c["id"]] +1

    # Count winners
    count = 0
    for n in c["numbers"]:
        if n in c["winners"]:
            count = count +1

    # Add the total tally of copies of the current card to the count of each 
    # future card affected. 
    for j in range(1, count+1):
        data[c["id"] + j] = data[c["id"] + j] + data[c["id"]]
        #cards.append(cards[cards[i]["id"] + j])

print(sum(data.values()))