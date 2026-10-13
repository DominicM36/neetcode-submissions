class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        #cur represents current list of numbers
        def dfs(i, cur, total):
            if total == target:
                #append combination
                #make sure its a copy so it doesnt mutate it
                res.append(cur.copy())
                return
            if i >= len(nums) or total > target:
                return
            #include nums[i]?
            cur.append(nums[i])
            dfs(i, cur, total + nums[i])
            cur.pop()
            #not including candidate
            dfs(i + 1, cur, total)
        dfs(0, [], 0)
        return res