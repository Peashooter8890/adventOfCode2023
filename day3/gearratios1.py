import re, os
location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

def isSymbol(char):
    pattern = r'[^\w\d\s.]'
    # I am going to try to make a habit of making sure function values return in a specific type
    return bool(re.match(pattern,char))

def hasNeighborSymbol(part,current,prev,next):
    index = part[0]
    charLen = len(part[1])
    left = 1 if index == 0 else 0
    right = 1 if index == len(current) - 1 else 0
    # check the current line
    if not left:
        if isSymbol(current[index-1]):
            return True
    if not right:
        if isSymbol(current[index+charLen]):
            return True
    # check previous and next line
    if prev:
        for i in range(left-1, charLen + 1 - right):
            if isSymbol(prev[index + i]):
                return True
    if next:
        for i in range(left-1, charLen + 1 - right):
            if isSymbol(next[index + i]):
                return True
    return False
        
with open(os.path.join(location, "gearratios.txt"), "r") as file:
    lines = file.readlines()

sum = 0

for i, line in enumerate(lines):
    prevLine = lines[i - 1] if i > 0 else None
    nextLine = lines[i + 1] if i < len(lines) - 1 else None
    nums = []
    num_seq = ""
    add_condition = False
    for j, char in enumerate(line):
        if char.isdigit():
            num_seq += char
            add_condition = True
        else:
            if add_condition == True:
                nums.append((j - len(num_seq),num_seq))
                num_seq = ""
                add_condition = False
    for num in nums:
        if hasNeighborSymbol(num, line, prevLine, nextLine):
            sum += int(num[1])
print(sum)