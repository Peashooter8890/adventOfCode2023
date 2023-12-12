import os
location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
instructions = 'LRLRRRLRRRLLLRLRRLLRLRRRLRLRRRLRLRRRLRLRRRLRRRLRLLRRRLRLRLRRLRRLRLRRLRRLRRLLRRRLRRRLRRLRRLRRLRRRLLRRLRLRRLRLRRLRRLRLRRLRRLLRLRRRLRRLRRRLLRLRLRLLRLLRLLRLRRLLRRLRLRLRRLRLLRRRLLRRRLRRLLRRRLRRRLRLRRRLLRRRLRLRRRLLLRRRLRLRLRRRLRRRLRRRLRLRRLLLRRLRRRLLRLRRRLRLRLLLRRLRLRRRLRLRRRR'

allTiles = {}
maxI, maxJ = None, None

def edgeDetection(start):
    global maxI, maxJ
    left, right, top, bottom = True, True, True, True
    if not start[1][0]:
        top = False
    if start[1][0] == maxI:
        bottom = False
    if not start[1][1]:
        left = False
    if start[1][1] == maxJ:
        right = False
    return left, right, top, bottom

def detectNeighbors(start, unsearched):
    global allTiles
    northNeighbors = ["|","7","F"]
    southNeighbors = ["|","L","J"]
    eastNeighbors = ["-","J","7"]
    westNeighbors = ["-","L","F"]
    left, right, top, bottom = edgeDetection(start)
    i, j = start[1][0],start[1][1]
    neighbors = []
    if top:
        neighbors.append(allTiles[(i+1,j)]) if allTiles[(i+1,j)] in northNeighbors else None
        if left:
            neighbors.append(allTiles[(i+1,j-1)]) if allTiles[(i+1,j-1)] in westNeighbors else None
        if right:
            neighbors.append(allTiles[(i+1,j+1)]) if allTiles[(i+1,j+1)] in eastNeighbors else None
    if bottom:
        neighbors.append(allTiles[(i-1,j)]) if allTiles[(i-1,j)] in southNeighbors else None
        if left:
            neighbors.append(allTiles[(i-1,j-1)]) if allTiles[(i-1,j-1)] in westNeighbors else None
        if right:
            neighbors.append(allTiles[(i-1,j+1)]) if allTiles[(i-1,j+1)] in eastNeighbors else None
    if left:
        neighbors.append(allTiles[(i,j-1)]) if allTiles[(i,j-1)] in westNeighbors else None
    if right:
        neighbors.append(allTiles[(i,j+1)]) if allTiles[(i,j-1)] in eastNeighbors else None
    index = start[0] + 1
    unsearched.extend([(index, y) for _, y in neighbors])
    return unsearched

def computeFurthest(searched):
    locations, matches = [], []
    for tile in searched:
        locations.append(tile)
        if len(locations) != len(set(locations)):
            matches.append(tile)
            locations.pop()
    if matches:
        distances = [x[0] for x in matches]
        return max(distances)
    
def tileSearch(start,searched,unsearched,furthest):
    unsearched = detectNeighbors(start,unsearched)
    furthest = computeFurthest(searched)
    # BFS technique
    if len(unsearched) > 0:
        tileToSearch = min(unsearched, key=lambda x: x[0])
    else:
        return furthest
    searched.append(tileToSearch)
    return tileSearch(tileToSearch,searched,unsearched,furthest)

with open(os.path.join(location, "pipeMaze.txt"), "r") as f:
    start = None
    # apparently _ is a conventional name for a variable whose name will not be used
    maxI = sum(1 for _ in f)
    maxJ = len(f.readline())
    for i, line in enumerate(f):
        for j, char in enumerate(line):
            allTiles[(i,j)] = char
            if char == 'S':
                start = (0,(i,j))
    searched, unsearched = [start], []
    