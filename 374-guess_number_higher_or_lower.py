def guessNumber(n):
    lower, higher = 1, n
    while lower <= higher:
        mid = (lower+higher) // 2
        r = guess(mid)

        if r == 0:
            return mid
        elif r == -1:
            higher = mid - 1
        else:
            lower = mid + 1
    return -1