class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #idea is check water at each step
        #start two pointers at each end
        #depending on which pillar is taller, move other pointer

        l,r = 0, len(heights) - 1
        maxWater = 0

        while l < r:
            #cant just multiply the heights, the area is distance * height of lower
            
            if heights[l] < heights[r]:
                curWater = heights[l] * (r - l)
                maxWater = max(maxWater, curWater)
                l += 1
            else:
                curWater = heights[r] * (r-l)
                maxWater = max(maxWater, curWater)
                r -= 1
        return maxWater

