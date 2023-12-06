time = 56717999
distance = 334113513502430

waysToWin = 0
i = 0
while(True):
    half = int(time/2)
    if ((half-i) * (half + i + 1)) > distance:
        print(half-i)
        waysToWin += 1
    else:
        break
    i += 1

print(waysToWin * 2) # 43364472