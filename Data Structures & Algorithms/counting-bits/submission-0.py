class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n + 1):
            cur = i
            count = 0
            while cur:
                count += cur % 2
                cur = cur >> 1
            res.append(count)
        return res