def load_configuration(file_path):
    with open(file_path, "r") as f:
        lines = [l.strip() for l in f.readlines()]

        sequences = list(map(lambda x : list(map(lambda x : int(x), x.split(" "))), lines))
        
        return sequences

def produce_next_sequence(s):
    new_sequence = []

    if len(s) < 2:
        # Shouldn't happen.
        assert False
    
    for i in range(1, len(s)):
        new_sequence.append(s[i]-s[i-1])

    return new_sequence

def predict_next_value(s):
    seq = [s]
    while True:
        seq.append(produce_next_sequence(seq[-1]))

        if all([(x == 0) for x in seq[-1]]):
            break
 
    for i in reversed(range(0, len(seq)-1)):
        seq[i].append(seq[i][-1] + seq[i+1][-1])

    return seq[0][-1]
        
sequences = load_configuration("input.txt")

# Part 1
_sum = 0
for s in sequences:
    _sum = _sum + predict_next_value(s)

print(f"Solution - Part 1: {_sum}")

# Part 2