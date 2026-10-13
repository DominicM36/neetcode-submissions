class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_vals = {}

        for i,v in enumerate(nums):
            diff = target - v
            if diff in seen_vals:
                return[seen_vals[diff], i]
            seen_vals[v] = i