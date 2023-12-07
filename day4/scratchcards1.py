import os
location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

sum = 0

with open(os.path.join(location, "scratchcards.txt"), "r") as file:
    for line in file:
        winningCards = set([int(num.rstrip()) for num in line.split("|")[0].split(" ") if num.rstrip().isdigit()])
        ownedCards = set([int(num.rstrip()) for num in line.split("|")[1].split(" ") if num.rstrip().isdigit()])
        numOfGoodCards = len(winningCards.intersection(ownedCards))
        if numOfGoodCards == 0:
            continue
        else:
            sum += 2 ** (numOfGoodCards - 1)
print(sum)