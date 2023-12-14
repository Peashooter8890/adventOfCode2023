import os, copy
location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
allTiles = {}
allTilesNew = {}
loopTiles = {}
zeroLocations = {}
antiZeroLocations = {}
cardinalKeys = {
    'up': 'U',
    'down': 'D',
    'left': 'L',
    'right': 'R',
    'upright': '└',
    'upleft': '┐',
    'downright': '┌',
    'downleft': '┘'
}
inverseCardinalKeys = {v:k for k,v in cardinalKeys.items()}
rights = {'upright':None,'downright':None,'right':None}
lefts = {'upleft':None,'downleft':None,'left':None}
ups = {'upright':None,'upleft':None,'up':None}
downs = {'downright':None,'downleft':None,'down':None}
cardinalList = ['U','D','L','R','┐','┌','┘','└']
numOfEnclosedTiles = 0
maxI,maxJ = 0, 0

def computeTheFour(i,j):
    up, down, left, right = None, None, None, None
    iMinus = 1
    while i - iMinus > 0:
        if allTilesNew[(i-iMinus, j)] in cardinalList:
            up = allTilesNew[(i-iMinus, j)]
            break
        iMinus += 1
    iPlus = 1
    while i + iPlus < maxI-1:
        if allTilesNew[(i+iPlus, j)] in cardinalList:
            down = allTilesNew[(i+iPlus, j)]
            break
        iPlus += 1
    jMinus = 1
    while j - jMinus > 0:
        if allTilesNew[(i, j-jMinus)] in cardinalList:
            left = allTilesNew[(i, j-jMinus)]
            break
        jMinus += 1
    jPlus = 1
    while j + jPlus < maxJ-1:
        if allTilesNew[(i, j+jPlus)] in cardinalList:
            right = allTilesNew[(i, j+jPlus)]
            break
        jPlus += 1
    if (up and inverseCardinalKeys[up] in downs) or \
    (down and inverseCardinalKeys[down] in ups) or \
    (left and inverseCardinalKeys[left] in rights) or \
    (right and inverseCardinalKeys[right] in lefts):
        return 1
    elif (up and inverseCardinalKeys[up] in ups) or \
    (down and inverseCardinalKeys[down] in downs) or \
    (left and inverseCardinalKeys[left] in lefts) or \
    (right and inverseCardinalKeys[right] in rights):
        return -1
    return 0

def addToZeroLocation(loc):
    global zeroLocations
    if allTilesNew[loc] == '0':
        if loc not in zeroLocations:
            zeroLocations[loc] = '0'
            return 1
    return 0

def computeClusters(loc):
    counter = 0
    up, down, left, right = True, True, True, True
    i,j = loc[0],loc[1]
    if i == 0:
        up = False
    elif i == maxI-1:
        down = False
    if j == 0:
        left = False
    elif j == maxJ-1:
        right = False
    if up:
        counter += addToZeroLocation((i-1,j))
        if left:
            counter += addToZeroLocation((i-1,j-1))
        if right:
            counter += addToZeroLocation((i-1,j+1))
    if down:
        counter += addToZeroLocation((i+1,j))
        if left:
            counter += addToZeroLocation((i+1,j-1))
        if right:
            counter += addToZeroLocation((i+1,j+1))
    if left:
        counter += addToZeroLocation((i,j-1))
    if right:
        counter += addToZeroLocation((i,j+1))
    return counter

def traverse(direction, wallDirection, tile, index):
    global loopTiles
    # make these into dicts for hash map speed
    while True:
        tileValue = allTiles[tile]
        i, j = tile[0], tile[1]
        if tileValue == 'S':
            return
        if tileValue == '|':
            if direction == 'up':
                tile = (i-1,j)
            elif direction == 'down':
                tile = (i+1,j)
            if wallDirection in lefts:
                    wallDirection = 'left'
            elif wallDirection in rights:
                wallDirection = 'right'
        elif tileValue == '-':
            if direction == 'left':
                tile = (i,j-1)
            elif direction == 'right':
                tile = (i,j+1)
            if wallDirection in ups:
                    wallDirection = 'up'
            elif wallDirection in downs:
                wallDirection = 'down'
        elif tileValue == 'L':
            if direction == 'down':
                tile = (i,j+1)
                direction = 'right'
                if wallDirection in rights:
                    wallDirection = 'upright'
                elif wallDirection in lefts:
                    wallDirection = 'downleft'
            elif direction == 'left':
                tile = (i-1,j)
                direction = 'up'
                if wallDirection in ups:
                    wallDirection = 'upright'
                elif wallDirection in downs:
                    wallDirection = 'downleft'
        elif tileValue == 'J':
            if direction == 'down':
                tile = (i,j-1)
                direction = 'left'
                if wallDirection in lefts:
                    wallDirection = 'upleft'
                elif wallDirection in rights:
                    wallDirection = 'downright'
            elif direction == 'right':
                tile = (i-1,j)
                direction = 'up'
                if wallDirection in ups:
                    wallDirection = 'upleft'
                elif wallDirection in downs:
                    wallDirection = 'downright'
        elif tileValue == '7':
            if direction == 'up':
                tile = (i,j-1)
                direction = 'left'
                if wallDirection in lefts:
                    wallDirection = 'downleft'
                elif wallDirection in rights:
                    wallDirection = 'upright'
            elif direction == 'right':
                tile = (i+1,j)
                direction = 'down'
                if wallDirection in downs:
                    wallDirection = 'downleft'
                elif wallDirection in ups:
                    wallDirection = 'upright'
        elif tileValue == 'F':
            if direction == 'up':
                tile = (i,j+1)
                direction = 'right'
                if wallDirection in lefts:
                    wallDirection = 'upleft'
                elif wallDirection in rights:
                    wallDirection = 'downright'
            elif direction == 'left':
                tile = (i+1,j)
                direction = 'down'
                if wallDirection in ups:
                    wallDirection = 'upleft'
                elif wallDirection in downs:
                    wallDirection = 'downright'
        loopTiles[(i,j)] = wallDirection
        index += 1

with open(os.path.join(location, 'pipeMaze.txt'), 'r') as f:
    start = None
    maxI = sum(1 for _ in f) #?
    f.seek(0)
    maxJ = len(f.readline().rstrip()) #?
    f.seek(0)
    for i, line in enumerate(f):
        for j, char in enumerate(line):
            if char != '\n':
                allTiles[(i,j)] = char
            if char == 'S':
                start = (i,j)
    f.seek(0)

    # tile = (start[0], start[1]+1)
    tile = (start[0], start[1]+1)
    index = 1
    # direction, walldirection
    traverse('right', 'upright', tile, index)

with open(os.path.join(location, 'pipeMaze3.txt'), 'w') as nf:
    with open(os.path.join(location, 'pipeMaze.txt'), 'r') as f:
        for i, line in enumerate(f):
            newLine = ''
            for j, char in enumerate(line):
                if char == 'S':
                    newLine += 'S'
                elif (i, j) in loopTiles:
                    newLine += cardinalKeys[loopTiles[(i,j)]]
                elif char != '\n':
                    newLine += '0'
                else:
                    newLine += '\n'
            nf.write(newLine)

with open(os.path.join(location, 'pipeMaze3.txt'), 'r') as f:
    for i, line in enumerate(f):
        for j, char in enumerate(line):
            if char != '\n':
                allTilesNew[(i,j)] = char
    f.seek(0)

# this is so messy and useless but I don't care
grid = []
with open(os.path.join(location, 'pipeMaze3.txt'), 'r') as f:
    for line in f:
        grid.append(line)

for i, line in enumerate(grid):
    if not set(cardinalList).intersection(set(line)):
        continue
    if i == 0 or i == maxI-1:
        continue
    else:
        for j, char in enumerate(line):
            if char in cardinalList:
                leftChar = char
            if char == '0': 
                if computeTheFour(i,j) == 1:
                    zeroLocations[(i,j)] = '0'
                elif computeTheFour(i,j) == -1:
                    antiZeroLocations[(i,j)] = '0'

while True:
    counter = 0
    zeroLocationsCopy = copy.deepcopy(zeroLocations)
    for loc in zeroLocationsCopy:
        counter += computeClusters(loc)
    if counter == 0:
        break

with open(os.path.join(location, 'pipeMaze4.txt'), 'w') as nf:
    with open(os.path.join(location, 'pipeMaze3.txt'), 'r') as f:
        for i, line in enumerate(f):
            newLine = ''
            for j, char in enumerate(line):
                if (i, j) in loopTiles:
                    newLine += cardinalKeys[loopTiles[(i,j)]]
                elif char != '\n':
                    if (i, j) in zeroLocations:
                        newLine += '8'
                        numOfEnclosedTiles += 1
                    else:
                        newLine += '0'
                else:
                    newLine += '\n'
            nf.write(newLine)

with open(os.path.join(location, 'pipeMaze5.txt'), 'w') as nf:
    with open(os.path.join(location, 'pipeMaze2.txt'), 'r') as f:
        for i, line in enumerate(f):
            newLine = ''
            for j, char in enumerate(line):
                if (i,j) not in zeroLocations:
                    if (i,j) in antiZeroLocations:
                        newLine += ' '
                    else:
                        newLine += char
                else:
                    newLine += '8'
            nf.write(newLine)

with open(os.path.join(location, 'pipeMazeFinal.txt'), 'w') as nf:
    with open(os.path.join(location, 'pipeMaze5.txt'), 'r') as f:
        for line in f:
            newLine = ''
            for char in line:
                if char == '0':
                    newLine += ' '
                else:
                    newLine += char
            nf.write(newLine)

print(numOfEnclosedTiles)