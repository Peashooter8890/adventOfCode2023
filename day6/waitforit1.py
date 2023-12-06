times = [56, 71, 79, 99]
distances = [334, 1135, 1350, 2430]

for i, time in enumerate(times):
    waysToWin = 0
    for j in range(time+1):
        if ((j) * (time - j)) > distances[i]:
            waysToWin += 1
    print(waysToWin)