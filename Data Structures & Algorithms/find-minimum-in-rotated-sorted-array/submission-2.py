class Solution:
    def findMin(self, nums: List[int]) -> int:
        for i in range(len(nums) -1):
            if nums[i + 1] < nums[i]:
                return nums[i+1]
        #sorted array
        return nums[0]