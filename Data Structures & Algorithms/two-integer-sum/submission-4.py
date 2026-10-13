class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #keep an array of seen values and indices
        #need to create a map of indices of seen values
        indices = {}

        for i in range(len(nums)):
            dif = target - nums[i]
            #check if seen before
            if dif in indices:
                return [indices[dif], i]
            indices[nums[i]] = i
