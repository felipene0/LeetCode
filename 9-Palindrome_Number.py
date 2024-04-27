def isPalindrome(x):
    d = 1
    if x < 0:
        return False
    
    while x >= 10 * d:
        d *= 10

    while x:
        if x // d != x % 10:
            return False

        x = (x % d) // 10
        d /= 100
    return True

r = 1001
r = isPalindrome(r)
print(r)