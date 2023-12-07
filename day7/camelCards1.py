import os
location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

cardTypes = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]

def compareSameRankCards(card1, card2):
    for i, card in enumerate(card1[0]):
        card1Rank = cardTypes.index(card)
        card2Rank = cardTypes.index(card2[0][i])
        if card1Rank == card2Rank:
            continue
        elif card1Rank > card2Rank:
            return True
        else:
            return False
    return True
    

def rankHands(hands):
    listInSorting = []
    for hand in hands:
        if len(listInSorting) == 0:
            listInSorting.append(hand)
        else:
            for i, competitor in enumerate(listInSorting):
                if compareSameRankCards(hand,competitor):
                    if i < len(listInSorting) - 1:
                        continue
                    else:
                        listInSorting.insert(i+1,hand)
                        break
                else:
                    listInSorting.insert(i,hand)
                    break
    return listInSorting

handTypes = {
    "highCard": [],
    "onePair": [],
    "twoPairs": [],
    "threeOfKind": [],
    "fullHouse": [],
    "fourOfKind": [],
    "fiveOfKind": [],
}
allCardsRanked = []

with open(os.path.join(location, "camelCards.txt"), "r") as file:
    for line in file:
        hand = line.split(" ")[0]
        bid = line.split(" ")[1]
        occurences = []
        for type in cardTypes:
            occurences.append(hand.count(type))
        if max(occurences) == 1:
            handTypes["highCard"].append((hand,bid))
        if max(occurences) == 2:
            if occurences.count(2) == 2:
                handTypes["twoPairs"].append((hand,bid))
            else:
                handTypes["onePair"].append((hand,bid))
        if max(occurences) == 3:
            if occurences.count(2) == 1:
                handTypes["fullHouse"].append((hand,bid))
            else:
                handTypes["threeOfKind"].append((hand,bid))
        if max(occurences) == 4:
            handTypes["fourOfKind"].append((hand,bid))
        if max(occurences) == 5:
            handTypes["fiveOfKind"].append((hand,bid))
    for hands in handTypes.values():
        allCardsRanked.extend(rankHands(hands))

    sum = 0

    for i, hand in enumerate(allCardsRanked):
        sum += (i + 1) * int(hand[1])

print(sum)