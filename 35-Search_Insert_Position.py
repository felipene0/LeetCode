class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        for index, item in enumerate(nums):
            if item >= target:
                return index
        return len(nums)