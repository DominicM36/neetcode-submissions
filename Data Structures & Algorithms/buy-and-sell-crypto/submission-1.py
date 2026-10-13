class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #pointers to find when to buy or sell
        #profit = sell - buy
        #if next val is cheaper than buy val move buy
        #check max of profit at each step
        buyVal = prices[0]
        maxP = 0

        for i, v in enumerate(prices):
            maxP = max(maxP, v - buyVal)
            buyVal = min(buyVal, v)
        return maxP

        