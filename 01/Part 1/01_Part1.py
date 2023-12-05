
DIGITS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

with open("input.txt", "r") as f:
    lines = f.readlines()

grand_sum = 0

for l in lines:
    line = l.strip()

    concatenated_digit = ""
    for c in line:
        if c in DIGITS:
            concatenated_digit = concatenated_digit + c
            break

    for c in reversed(line):
        if c in DIGITS:
            concatenated_digit = concatenated_digit + c
            break

    grand_sum = grand_sum + int(concatenated_digit)

print(f"The grand sum is {grand_sum}")