import re, os
location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

def isCubeValid(unstructuredCube):
    cube = unstructuredCube.split()
    redNum, blueNum, greenNum = 12, 14, 13
    if cube[1] == "red":
        if int(cube[0]) <= redNum:
            return True
    if cube[1] == "blue":
        if int(cube[0]) <= blueNum:
            return True
    if cube[1] == "green":
        if int(cube[0]) <= greenNum:
            return True 
    return False

def main():
    sum = 0
    with open(os.path.join(location, "cubeConundrum.txt"), "r") as file:
        for i, line in enumerate(file):
            idIndex = line.find(":")
            fLine = line[(idIndex + 1):]
            isValid = True
            cubeList = [cube.strip() for cube in re.split(r'[;,]', fLine)]
            for cube in cubeList:
                if not isCubeValid(cube):
                    isValid = False
            if isValid:
                sum += (i+1)
    print(sum)

if __name__ == "__main__":
    main()