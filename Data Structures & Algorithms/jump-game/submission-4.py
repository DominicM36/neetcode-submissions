class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #keep shifting goal post until it reaches the end
        #start shifting goal anytime it is reached towards from
        goal = len(nums)-1

        for i in range(len(nums) -1, -1, -1):
            #can current position + value at position reach goal or over
            if i + nums[i] >= goal:
                goal = i

        if goal == 0:
            return True
        else:
            return False