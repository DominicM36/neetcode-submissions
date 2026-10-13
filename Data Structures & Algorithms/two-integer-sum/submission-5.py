class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #keep an array of seen values and indices
        #need to create a map of indices of seen values
        indices = {}
        for i in range(len(nums)):
            #to know target index, find difference from current value and search in map
            diff = target - nums[i]
            if diff in indices:
                return [indices[diff], i]
            #need to add to indices
            indices[nums[i]] = i
