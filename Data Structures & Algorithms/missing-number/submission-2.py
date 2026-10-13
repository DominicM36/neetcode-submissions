class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # numSet = {}
        # for i in range(len(nums)):
        #     numSet[i] = i
        # print(numSet)
        
        # for i in range(len(nums)):
        #     if nums[i] not in numSet:
        #         return i
        # return 0    
        res = len(nums)
        for i in range(len(nums)):
            res = res ^ i
        for i in range(len(nums)):
            res = res ^ nums[i]
        return res
