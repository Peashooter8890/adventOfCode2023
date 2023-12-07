import os
location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

sum = 0
cards = []

with open(os.path.join(location, "scratchcards.txt"), "r") as file:
    for line in file:
        winningCards = set([int(num.rstrip()) for num in line.split("|")[0].split(" ") if num.rstrip().isdigit()])
        ownedCards = set([int(num.rstrip()) for num in line.split("|")[1].split(" ") if num.rstrip().isdigit()])
        numOfGoodCards = len(winningCards.intersection(ownedCards))
        cards.append([numOfGoodCards, 1])

for i, card in enumerate(cards):
    matches = card[0]
    copies = card[1]
    for j in range(copies):
        for k in range(1, matches + 1):
            try:
                cards[i+k][1] += 1
            except:
                break

for card in cards:
    sum += card[1]

print(sum)