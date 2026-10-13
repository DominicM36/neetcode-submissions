class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        for i, v in enumerate(nums):
            if v in hashmap.keys():
                return True
            else:
                hashmap[v] = i
        return False