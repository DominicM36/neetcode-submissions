class Solution:
    def countBits(self, n: int) -> List[int]:
        # res = []
        # for i in range(n + 1):
        #     cur = i
        #     count = 0
        #     while cur:
        #         count += cur % 2
        #         cur = cur >> 1
        #     res.append(count)
        # return res

        #o(nlogn) above, can do better with DP

        #for DP the idea is take each significant bit section and for all the bits between significant bits
        #add the already known values so no need to recalculate
        #sig bits can be calculated if n = 2*prev sig bit (i.e does 3 = 2*2)
        #sig bit starts at 1, 1*2 is 2 at two sig bit oves to two, 2*2 = 4 at 4 sig bit moves to 4

        dp = [0]*(n+1)
        sigBit = 1
        for i in range(1, n+1):
            if i == sigBit*2:
                sigBit = i
            dp[i] = 1 + dp[i-sigBit]
        return dp





