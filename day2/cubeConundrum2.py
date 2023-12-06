import re,os
location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

def divideCubes(cubeList):
    reds, blues, greens = [], [], []
    for cube in cubeList:
        if re.match(redex,cube):
            reds.append(int(cube.split()[0]))
            continue
        if re.match(blueex,cube):
            blues.append(int(cube.split()[0]))
            continue
        if re.match(greenex,cube):
            greens.append(int(cube.split()[0]))
    return max(reds), max(blues), max(greens)

redex = r"^\d+ (red)$"
blueex = r"^\d+ (blue)$"
greenex = r"^\d+ (green)$"

def main():
    sum = 0
    with open(os.path.join(location, "cubeConundrum.txt"), "r") as file:
        sum = 0
        for line in file:
            idIndex = line.find(":")
            fLine = line[(idIndex + 1):]
            cubeList = [cube.strip() for cube in re.split(r'[;,]', fLine)]
            red, blue, green = divideCubes(cubeList)
            sum += (red * blue * green)
    print(sum)

if __name__ == "__main__":
    main()