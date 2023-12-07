import os
location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

def getNeighborDigits(index,current,prev,next):
    currentIndices, prevIndices, nextIndices = [], [], []
    left = 1 if index == 0 else 0
    right = 1 if index == len(current) - 1 else 0
    if not left:
        neighbor = current[index-1]
        if neighbor.isdigit():
            currentIndices.append(index-1)
    if not right:
        neighbor = current[index+1]
        if neighbor.isdigit():
            currentIndices.append(index+1)
    if prev:
        for i in range(left - 1, 2 - right):
            neighbor = prev[index+i]
            if neighbor.isdigit():
                prevIndices.append(index+i)
    if next:
        for i in range(left - 1, 2 - right):
            neighbor = next[index+i]
            if neighbor.isdigit():
                nextIndices.append(index+i)
    return currentIndices, prevIndices, nextIndices

def returnLineNums(lines):
    lineNums = []
    for line in lines:
        nums = []
        num_seq = ""
        add_condition = False
        for j, char in enumerate(line):
            if char.isdigit():
                num_seq += char
                add_condition = True
            else:
                if add_condition == True:
                    nums.append((j - len(num_seq), j, num_seq))
                    num_seq = ""
                    add_condition = False
        lineNums.append(nums)
    return lineNums
        
with open(os.path.join(location, "gearratios.txt"), "r") as file:
    lines = file.readlines()

lineNums = returnLineNums(lines)
sum = 0

for i, line in enumerate(lines):
    prevLine = lines[i - 1] if i > 0 else None
    nextLine = lines[i + 1] if i < len(lines) - 1 else None
    for j, char in enumerate(line):
        numbers = set()
        if char == "*":
            currentIndices, prevIndices, nextIndices = getNeighborDigits(j,line,prevLine,nextLine)
            for index in currentIndices:
                for num in lineNums[i]:
                    if index >= num[0] and index <= num[1]:
                        numbers.add(int(num[2]))
            if i != 0:
                for index in prevIndices:
                    for num in lineNums[i-1]:
                        if index >= num[0] and index <= num[1]:
                            numbers.add(int(num[2]))
            if i != len(lines) - 1:
                for index in nextIndices:
                    for num in lineNums[i+1]:
                        if index >= num[0] and index <= num[1]:
                            numbers.add(int(num[2]))
            if len(numbers) == 2:
                x, y = numbers
                sum += x * y

print(sum)