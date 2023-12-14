import os
location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

def doubleTheSpaces(matrix):
    rowsToAdd, columnsToAdd = [], []
    # get column and row indices
    for i, row in enumerate(matrix):
        if '#' not in row:
            rowsToAdd.append(i)
            # *zip(*matrix) transposes a matrix
    for i, row in enumerate([*zip(*matrix)]):
        if '#' not in row:
            columnsToAdd.append(i)
    newMatrix = []
    for i, row in enumerate(matrix):
        newMatrix.append(row)
        if i in rowsToAdd:
            newMatrix.append(('.',)*len(row))
    matrix = [*zip(*newMatrix)]
    newMatrix = []
    for i, row in enumerate(matrix):
        newMatrix.append(row)
        if i in columnsToAdd:
            newMatrix.append(('.',)*len(row))
    return [*zip(*newMatrix)]

def getGalaxyLocations(matrix):
    galaxyLocations = []
    for i, row in enumerate(matrix):
        galaxyLocations.extend([(i, j) for j, x in enumerate(row) if x == '#'])
    return galaxyLocations

def computeDistances(galaxyLocations):
    counter = 0
    sumOfDistances = 0
    while True:
        if len(galaxyLocations) == 0:
            print("num of pairs is ", counter)
            return sumOfDistances
        distances = 0
        galaxy = galaxyLocations.pop(0)
        for otherGalaxy in galaxyLocations:
            counter += 1
            distances += abs(galaxy[0] - otherGalaxy[0]) + abs(galaxy[1] - otherGalaxy[1])
        sumOfDistances += distances


matrix = []
with open(os.path.join(location, "cosmicExpansion.txt"), "r") as f:
    for i, line in enumerate(f):
        matrix.append(tuple(line))
matrix = doubleTheSpaces(matrix)
galaxyLocations = getGalaxyLocations(matrix)
sumOfDistances = computeDistances(galaxyLocations)
print(sumOfDistances)