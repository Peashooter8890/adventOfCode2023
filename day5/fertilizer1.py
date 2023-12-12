import os
location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
almanac = []
locations = []

def mapper(x, index, almanac):
    mapped = None
    for map in almanac:
        if x >= map[1] and x <= map[1] + map[2]:
            mapped = map[0] + (x - map[1])
            break
    if not mapped:
        mapped = x
    if index == len(almanac) - 1:
        return mapped
    return mapper(mapped, index+1, almanac)

with open(os.path.join(location, "test.txt"), "r") as file:
    map = []
    for i, line in enumerate(file):
        if line.strip() == "" or i == len(file.readlines()) - 1:
            almanac.append(map)
            map = []
            break
        map.append([int(x) for x in line.split(" ")])
        
    seeds = [364807853, 408612163, 302918330, 20208251, 1499552892, 200291842, 3284226943, 16030044, 2593569946, 345762334, 3692780593, 17215731, 1207118682, 189983080, 2231594291, 72205975, 3817565407, 443061598, 2313976854, 203929368]
    seeds = [79, 14, 55, 13]
    for seed in seeds:
        locations.append(mapper(seed, 0, almanac))

print(min(locations))