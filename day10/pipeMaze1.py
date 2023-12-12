import os
location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
allTiles = {}

def traverse(direction, tile, index):
    tileValue = allTiles[tile]
    i, j = tile[0], tile[1]
    if tileValue == 'S':
        return index
    elif tile == '.':
        pass
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
    return traverse(direction, tile, index)

with open(os.path.join(location, 'pipeMaze.txt'), 'r') as f:
    start = None
    # apparently _ is a conventional name for a variable whose name will not be used
    maxI = sum(1 for _ in f)
    f.seek(0) # reset file pointer because the file is already all read now
    maxJ = len(f.readline())
    f.seek(0)
    for i, line in enumerate(f):
        for j, char in enumerate(line):
            if char != '\n':
                allTiles[(i,j)] = char
            if char == 'S':
                start = (i,j)

    # I can use ctrl + f to find what the two valid neigbors of S is. 
    # Those neighbors are to the left and to the right precisely. Start with left. Just do DFS.
    # With DFS, complete loop, then round up steps / 2.
    # Therefore I shall do this part manually.

    tile = (start[0], start[1]-1)
    index = 1
    steps = traverse('left', tile, index)

print(round(steps/2.0))