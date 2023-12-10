
with open("example.txt", "r") as f:
    lines = f.readlines()

seeds = [x for x in map(lambda x : int(x.strip()), list(filter(None, lines[0].split(":")[1].split(" "))))]

lines = list(map(lambda x : x.strip(), lines))


# parsing configuration
line_numbers = {}

for i, l in enumerate(lines):
    if l == "seed-to-soil map:":
        line_numbers["seed-to-soil"] = i
    elif l == "soil-to-fertilizer map:":
        line_numbers["soil-to-fertilizer"] = i
    elif l == "fertilizer-to-water map:":
        line_numbers["fertilizer-to-water"] = i
    elif l == "water-to-light map:":
        line_numbers["water-to-light"] = i
    elif l == "light-to-temperature map:":
        line_numbers["light-to-temperature"] = i
    elif l == "temperature-to-humidity map:":
        line_numbers["temperature-to-humidity"] = i
    elif l == "humidity-to-location map:":
        line_numbers["humidity-to-location"] = i
    

def mapping_from_configuration(lines):
    mapping = []
    for l in lines:
        split = l.split(" ")

        source = int(split[1])

        destination = int(split[0])

        length = int(split[2])

        mapping.append({
            "source": source,
            "dest": destination,
            "length": length
        })

    return sorted(mapping, key = lambda x : x["source"])
    

mappings = []
mappings.append(mapping_from_configuration(lines[(line_numbers["seed-to-soil"]+1):(line_numbers["soil-to-fertilizer"]-1)]))
mappings.append(mapping_from_configuration(lines[(line_numbers["soil-to-fertilizer"]+1):(line_numbers["fertilizer-to-water"]-1)]))
mappings.append(mapping_from_configuration(lines[(line_numbers["fertilizer-to-water"]+1):(line_numbers["water-to-light"]-1)]))
mappings.append(mapping_from_configuration(lines[(line_numbers["water-to-light"]+1):(line_numbers["light-to-temperature"]-1)]))
mappings.append(mapping_from_configuration(lines[(line_numbers["light-to-temperature"]+1):(line_numbers["temperature-to-humidity"]-1)]))
mappings.append(mapping_from_configuration(lines[(line_numbers["temperature-to-humidity"]+1):(line_numbers["humidity-to-location"]-1)]))
mappings.append(mapping_from_configuration(lines[(line_numbers["humidity-to-location"]+1):]))


# Part 1
locations = []

for s in seeds:
    value = s
    for m in mappings:
        #print(value)
        for bucket in m:
            if value >= bucket["source"]:
                if value <= bucket["source"] + bucket["length"]:
                    value = bucket["dest"] + (value - bucket["source"])
                    break
            
            # Otherwise value is unaltered.

    locations.append(value)

print(f"Lowest location value: {min(locations)}")

# Part 2
locations = []
i=0
buckets = []
while i*2+1 < len(seeds):
    print(i)
    bucket_start = seeds[i*2]
    bucket_length = seeds[i*2+1]

    buckets.append([bucket_start, bucket_length])

    i = i+1

print(buckets)