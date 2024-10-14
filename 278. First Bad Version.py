# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
class Solution:
    def firstBadVersion(self, n: int) -> int:
        hi = n
        lo = 0

        while (lo < hi):
            m = (lo + hi)//2
            if(isBadVersion(m)):
                hi = m
            else:
                lo = m + 1
            
        return lo