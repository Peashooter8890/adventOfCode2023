import os

def convertWordToNum(word):
    match word.lower():
        case "one":
            return 1
        case "two":
            return 2
        case "three":
            return 3
        case "four":
            return 4
        case "five":
            return 5
        case "six":
            return 6
        case "seven":
            return 7
        case "eight":
            return 8
        case "nine":
            return 9
    return None

def sortWordsByIndexKey(words):
    # make a list of tuples. I don't know why I didn't take this approach earlier - my code is so ugly
    # probably should fix this code later after I catch up with other challenges
    orderedWordTuples = [(word[0], int(word[1:])) for word in words]
    orderedWordTuples.sort(key=lambda x: x[1])
    return [word[0] for word in orderedWordTuples]

def computeTrebuchet(line):
    numbers = []
    for c in line:
        if c.isnumeric():
            numbers.append(c)
    return int(str(numbers[0]) + str(numbers[len(numbers)-1]))

def computeTrebuchet2(line):
    wordNums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    numbers = []
    unorderedWords = []
    numIndices = []
    wordIndices = []
    for i, c in enumerate(line):
        if c.isnumeric():
            numbers.append(c)
            numIndices.append(i)
    for i, word in enumerate(wordNums):
        start = 0
        while True:
            # this is so that if there are more than one occurences of the same word, all of them are listed
            index = line.find(word, start)
            if index == -1:
                break
            unorderedWords.append(str(convertWordToNum(word)) + str(index))
            wordIndices.append(index)
            start = index + 1
    words = sortWordsByIndexKey(unorderedWords)
    if len(wordIndices) != 0:
        minIndex = min(min(numIndices),min(wordIndices))
    else: 
        minIndex = min(numIndices)
    if len(wordIndices) != 0:
        maxIndex = max(max(numIndices),max(wordIndices))
    else:
        maxIndex = max(numIndices)

    answer = ""

    if minIndex in wordIndices:
        answer += words[0]
    else: 
        answer += numbers[0]
    if maxIndex in wordIndices:
        answer += words[-1]
    else: 
        answer += numbers[-1]
    
    return int(answer)

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

def part1():
    sum = 0
    with open(os.path.join(__location__, 'trebuchet.txt'), "r") as file:
        for line in file:
            sum += computeTrebuchet(line)
    print(sum)

def part2():
    # should print 613
    sum = 0
    with open(os.path.join(__location__, 'trebuchet.txt'), "r") as file:
        for line in file:
            sum += computeTrebuchet2(line)
    print(sum)

part1()
part2()

# 4, 6 has problem