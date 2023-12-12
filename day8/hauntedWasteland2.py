import os, re
location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
instructions = "LRLRRRLRRRLLLRLRRLLRLRRRLRLRRRLRLRRRLRLRRRLRRRLRLLRRRLRLRLRRLRRLRLRRLRRLRRLLRRRLRRRLRRLRRLRRLRRRLLRRLRLRRLRLRRLRRLRLRRLRRLLRLRRRLRRLRRRLLRLRLRLLRLLRLLRLRRLLRRLRLRLRRLRLLRRRLLRRRLRRLLRRRLRRRLRLRRRLLRRRLRLRRRLLLRRRLRLRLRRRLRRRLRRRLRLRRLLLRRLRRRLLRLRRRLRLRLLLRRLRLRRRLRLRRRR"

nodes = {}
iteratingNodes = []
start = None
highestTime = 0

with open(os.path.join(location, "hauntedWasteland.txt"), "r") as file:
    for line in file:
        key = re.sub(r'\W+', '', line.split("(")[0])
        left = re.sub(r'\W+', '', line.split("(")[1].split(",")[0])
        right = re.sub(r'\W+', '', line.split("(")[1].split(",")[1].rstrip())
        threeTuple = (key, left, right)
        if key[2] == "A":
            iteratingNodes.append(key)
        nodes[key] = threeTuple
    
allIsZ = False
i = 0
count = 0

while not allIsZ:
    allIsZ = True
    counter = 0
    j = 0
    for nodeKey in iteratingNodes:
        node = nodes[nodeKey]
        if node[0][2] != "Z":
            if (counter >= 2):
                print("FUCK, counter is ", counter)
            allIsZ = False
        if instructions[i] == "L":
            iteratingNodes[j] = node[1]
        elif instructions[i] == "R":
            iteratingNodes[j] = node[2]
        j += 1
        if allIsZ:
            counter += 1

    i = (i + 1) % len(instructions)
    count += 1

print(count)