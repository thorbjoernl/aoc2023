with open("input.txt", "r") as f:
    lines = f.readlines()

times = [x for x in map(lambda x : int(x.strip()), list(filter(None, lines[0].split(" ")[1:])))]

record_distances = [x for x in map(lambda x : int(x.strip()), list(filter(None, lines[1].split(" ")[1:])))]


print(times)
print(record_distances)

# Part 1
product = 1

for time, record in zip(times, record_distances):
    count = 0
    for hold_duration in range(0, time):
        distance = (time-hold_duration)*hold_duration

        if distance > record:
            count = count +1

    product = product * count

print(f"Part 1 solution: {product}")

# Part 2
time = int("".join([str(x) for x in times]))
record = int("".join([str(x) for x in record_distances]))

print(time, distance)

count = 0
for hold_duration in range(0, time):
    distance = (time-hold_duration)*hold_duration

    if distance > record:
        count = count +1


print(f"Part 2 solution: {count}")
