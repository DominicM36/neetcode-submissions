class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #keep an array of seen values and indices
        #need to create a map of indices of seen values
        seen = {}
        #key is index, values is value
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in seen:
                return [seen[diff], i]
            seen[nums[i]] = i
        return []