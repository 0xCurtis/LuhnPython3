#Made by 0xCurtis
def checkLuhn(card):
    nSum = 0
    for i in range(len(card) - 1, -1, -1):
        d = ord(card[i]) - ord('0')
        if (i%2 == 0):
            d = d * 2
        nSum += d // 10
        nSum += d % 10
    if (nSum % 10 == 0):
        return True
    else:
        return False