class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #binary search again

        l,r = 0, len(nums) - 1

        #need to loop through and check which side is sorted aka find the pivot
        while l <= r:
            m = l + (r-l) // 2
            if nums[m] == target:
                return m
            # with every m one half is sorted
            #left is sorted
            if nums[l] <= nums[m]:
                #is target in this side?
                if target >= nums[l] and target <= nums[m]:
                    #target is in sorted array
                    r = m
                else: 
                    l = m + 1
            #right half is sorted half
            else:
                if target > nums[m] and target <= nums[r]:
                    #target is in right sorted
                    l = m + 1
                else:
                    r = m


        return -1   

