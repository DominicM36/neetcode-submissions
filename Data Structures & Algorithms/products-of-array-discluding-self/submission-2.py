class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #can do this by finding prefix and postfix up until a certain point and store in output array. 

        output = []
        #starting with prefix
        prefix = 1
        #iter through 0-end of array
        for i in range(len(nums)):
            output.append(prefix)
            prefix = prefix * nums[i]

        #now go backwards for postfix
        postfix = 1
        for i in range(len(nums) -1, -1, -1):
            output[i] = output[i]*postfix
            postfix = postfix * nums[i]

        return output