def missingNumber(nums):
    leng = len(nums)
    total = sum(nums)
    nnums = (leng * (leng + 1)) // 2
    return nnums - total

print(missingNumber([3,0,1]))