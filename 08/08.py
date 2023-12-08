
def load_configuration(file_path):
    with open(file_path, "r") as f:
        lines = [l.strip() for l in f.readlines()]

        instruction_string = lines[0]

        mapping = {}
        for l in lines[2:]:
            split = l.split("=")

            position = split[0].strip()

            split2 = split[1].split(",")

            left = split2[0].replace("(", "").strip()
            right= split2[1].replace(")", "").strip()

            mapping[position] = (left, right)

        return instruction_string, mapping

instruction, mapping = load_configuration("input.txt")

position = "AAA"
index = 0

def get_instruction(instruction, index):
    return instruction[index % len(instruction)]

while position != "ZZZ":
    if get_instruction(instruction, index) == "L":
        position = mapping[position][0]
    elif get_instruction(instruction, index) == "R":
        position = mapping[position][1]
    else:
        assert False

    index = index +1
    
print(f"Solution - Part 1: {index}")

