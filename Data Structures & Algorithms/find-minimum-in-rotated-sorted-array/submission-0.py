class Solution:
    def findMin(self, nums: List[int]) -> int:
        sortedn = sorted(nums)

        if len(sortedn) == 0:
            return 0
        return sortedn[0]