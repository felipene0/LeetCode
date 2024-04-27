def twoSum(nums, target):
    hash = {}

    for i, n in enumerate(nums):
        diff = target - n
        if diff in hash:
            return [hash[diff], i]
        hash[n] = i

nums = [10,2,3,5]
target = 7

result = twoSum(nums, target)
print(result)