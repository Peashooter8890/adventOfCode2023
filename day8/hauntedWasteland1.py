import os, re
location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
instructions = "LRLRRRLRRRLLLRLRRLLRLRRRLRLRRRLRLRRRLRLRRRLRRRLRLLRRRLRLRLRRLRRLRLRRLRRLRRLLRRRLRRRLRRLRRLRRLRRRLLRRLRLRRLRLRRLRRLRLRRLRRLLRLRRRLRRLRRRLLRLRLRLLRLLRLLRLRRLLRRLRLRLRRLRLLRRRLLRRRLRRLLRRRLRRRLRLRRRLLRRRLRLRRRLLLRRRLRLRLRRRLRRRLRRRLRLRRLLLRRLRRRLLRLRRRLRLRLLLRRLRLRRRLRLRRRR"

nodes = []
start = None

def findNode(key, nodes):
    target = None
    i = 0
    while target != key:
        if nodes[i][0] == key:
            return nodes[i]
        else:
            i += 1

with open(os.path.join(location, "hauntedWasteland.txt"), "r") as file:
    for line in file:
        key = re.sub(r'\W+', '', line.split("(")[0])
        left = re.sub(r'\W+', '', line.split("(")[1].split(",")[0])
        right = re.sub(r'\W+', '', line.split("(")[1].split(",")[1].rstrip())
        nodes.append((key, left, right))
        if key == "AAA":
            start = (key, left, right)
    
count = 0
i = 0
currentNode = start
key = currentNode[0]
while key != "ZZZ":
    if instructions[i] == "L":
        currentNode = findNode(currentNode[1], nodes)
    elif instructions[i] == "R":
        currentNode = findNode(currentNode[2], nodes)
    key = currentNode[0]
    i += 1
    count += 1
    if i == len(instructions):
        i = 0

print(count)