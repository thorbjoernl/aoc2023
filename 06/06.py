import math
with open("input.txt", "r") as f:
    lines = f.readlines()

times = [x for x in map(lambda x : int(x.strip()), list(filter(None, lines[0].split(" ")[1:])))]

record_distances = [x for x in map(lambda x : int(x.strip()), list(filter(None, lines[1].split(" ")[1:])))]

def quadratic_equation(a, b, c):
    x1 = (-b + math.sqrt(b**2-(4*a*c)))/(2*a)
    x2 = (-b - math.sqrt(b**2-(4*a*c)))/(2*a)
    return x1, x2

factors = []
for duration, distance in zip(times, record_distances):
    a = -1
    b = duration
    c = -distance
    bound1, bound2 = quadratic_equation(a, b, c)

    factors.append(abs(int(bound1)-int(bound2)))

print(f"Part 1 solution: {math.prod(factors)}")

# Part 2
time = int("".join([str(x) for x in times]))
record = int("".join([str(x) for x in record_distances]))

a = -1
b = time
c = -record
bound1, bound2 = quadratic_equation(a, b, c)

print(f"Part 2 solution: {abs(int(bound1)-int(bound2))}")

