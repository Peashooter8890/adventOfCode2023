import os
location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
allTiles = {}
loopTiles = []

def traverse(direction, tile, index):
    global loopTiles
    while True:
        loopTiles.append(tile)
        tileValue = allTiles[tile]
        i, j = tile[0], tile[1]
        if tileValue == 'S':
            return index
        elif tileValue == '|':
            if direction == 'up':
                tile = (i-1,j)
            elif direction == 'down':
                tile = (i+1,j)
        elif tileValue == '-':
            if direction == 'left':
                tile = (i,j-1)
            elif direction == 'right':
                tile = (i,j+1)
        elif tileValue == 'L':
            if direction == 'down':
                tile = (i,j+1)
                direction = 'right'
            elif direction == 'left':
                tile = (i-1,j)
                direction = 'up'
        elif tileValue == 'J':
            if direction == 'down':
                tile = (i,j-1)
                direction = 'left'
            elif direction == 'right':
                tile = (i-1,j)
                direction = 'up'
        elif tileValue == '7':
            if direction == 'up':
                tile = (i,j-1)
                direction = 'left'
            elif direction == 'right':
                tile = (i+1,j)
                direction = 'down'
        elif tileValue == 'F':
            if direction == 'up':
                tile = (i,j+1)
                direction = 'right'
            elif direction == 'left':
                tile = (i+1,j)
                direction = 'down'
        index += 1

with open(os.path.join(location, 'pipeMaze.txt'), 'r') as f:
    start = None
    maxI = sum(1 for _ in f)
    f.seek(0)
    maxJ = len(f.readline())
    f.seek(0)
    for i, line in enumerate(f):
        for j, char in enumerate(line):
            if char != '\n':
                allTiles[(i,j)] = char
            if char == 'S':
                start = (i,j)
    f.seek(0)

    tile = (start[0], start[1]-1)
    index = 1
    steps = traverse('left', tile, index)

with open(os.path.join(location, 'pipeMaze2.txt'), 'w') as nf:
    with open(os.path.join(location, 'pipeMaze.txt'), 'r') as f:
        for i, line in enumerate(f):
            newLine = ''
            for j, char in enumerate(line):
                if (i, j) in loopTiles:
                    if char == "F":
                        newLine += "┌"
                    elif char == "7":
                        newLine += "┐"
                    elif char == "L":
                        newLine += "└"
                    elif char == "J":
                        newLine += "┘"
                    else:
                        newLine += char
                elif char != '\n':
                    newLine += '0'
                else:
                    newLine += '\n'
            nf.write(newLine)
