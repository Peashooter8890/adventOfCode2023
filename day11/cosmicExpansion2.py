import os
location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

def getGalaxyLocations(matrix):
    galaxyLocations = []
    for i, row in enumerate(matrix):
        galaxyLocations.extend([[i, j] for j, x in enumerate(row) if x == '#'])
    return galaxyLocations

def getLocationsAfterExpansion(matrix):
    emptyRows, emptyColumns = [], []
    for i, row in enumerate(matrix):
        if '#' not in row:
            emptyRows.append(i)
    for i, row in enumerate([*zip(*matrix)]):
        if '#' not in row:
            emptyColumns.append(i)
    galaxyLocations = getGalaxyLocations(matrix)
    for location in galaxyLocations:
        previousExpansionRows = sum(1 for index in emptyRows if location[0] > index)
        previousExpansionColumns = sum(1 for index in emptyColumns if location[1] > index)
        expansionAmount = 999999
        addedRows = previousExpansionRows * expansionAmount
        addedColumns = previousExpansionColumns * expansionAmount
        location[0] += addedRows
        location[1] += addedColumns
    return galaxyLocations

def computeDistances(galaxyLocations):
    counter = 0
    sumOfDistances = 0
    while True:
        if len(galaxyLocations) == 0:
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
        matrix.append(list(line))

galaxyLocations = getLocationsAfterExpansion(matrix)
sumOfDistances = computeDistances(galaxyLocations)
print(sumOfDistances)