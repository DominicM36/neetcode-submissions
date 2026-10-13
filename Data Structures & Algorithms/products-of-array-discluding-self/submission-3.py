class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #postfix and prefix array

        output = []
        prefix = 1
        for i in range(len(nums)):
            output.append(prefix)
            prefix = prefix * nums[i]
        #postfix array back into output, go backwards
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            output[i] = output[i] * postfix
            postfix *= nums[i]
        return output