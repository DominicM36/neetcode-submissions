class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = 0
        res = nums[0]
        for n in nums:
            curr_sum += n
            res = max(res, curr_sum)
            if curr_sum < 0:
                curr_sum = 0
        return res