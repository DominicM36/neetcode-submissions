class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #solve it two pointer way
        #sort the array first, then check for pointers within to get values

        res = []
        nums.sort()

        for i,v in enumerate(nums):
            if i > 0 and v == nums[i-1]:
                continue
            l,r = i + 1, len(nums) -1
            
            #first check, does the total = 0
            while l < r:
                if v + nums[l] + nums[r] == 0:
                    res.append([v, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l+=1
                #too small, move left pointer
                elif v + nums[l] + nums[r] < 0:
                    l += 1
                else: # v + nums[l] + nums[r] > 0:
                    r -= 1
        return res
                


