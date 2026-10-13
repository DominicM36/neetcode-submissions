class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #can sort input array to use two pointer 2 sum method for nlogn time

        res = []
        nums.sort()
        for i,v in enumerate(nums):
            if v > 0:
                break
            if i > 0 and v == nums[i-1]:
                continue
            l = i + 1
            r = len(nums) - 1 
            while l < r:
                #if result is greater than zero, move r
                if ((v + nums[l] + nums[r]) > 0):
                    r -= 1
                elif ((v + nums[l] + nums[r]) < 0):
                    l += 1
                else:
                    #equal 0
                    res.append([v,nums[l],nums[r]])
                    l+=1
                    r-=1
                    while(nums[l] == (nums[l-1]) and l < r):
                        l += 1
        return res
