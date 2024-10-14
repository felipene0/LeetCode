import math

def isPerfectSquare(num: int) -> bool:
        lo = 1 
        hi = num

        if num < 2:
            return True

        while (lo < hi):
            me = (hi + lo)//2

            if((me ** 2) == num):
                return True
            elif((me ** 2) > num):
                hi = me
            else:
                lo = me + 1
        return False