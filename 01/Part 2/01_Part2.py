import re

pattern = r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))"

with open("input.txt", "r") as f:
    lines = f.readlines()

# Generate lookup table to convert from match (which is digit or string) to
# digit string.
lookup_table = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}
for i in range(0, 10):
    lookup_table[str(i)] = str(i)

_sum = 0

for l in lines:
    matches = re.findall(pattern, l)
    digit1 = lookup_table[matches[0]]
    digit2 = lookup_table[matches[-1]]

    _sum = _sum + int(digit1 + digit2)
    print(f"For line, {l}, the calibration value {digit1 + digit2} was found.\nThe new grand sum is {_sum}.")

    