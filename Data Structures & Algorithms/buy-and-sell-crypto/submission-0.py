class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buy,sell = 0,1 #pointers for the array, buy,sell
        maxProfit = 0 #starting profit

        while sell < len(prices):
            #is it a profitable exchange?
            if prices[buy] < prices[sell]:
                profit = prices[sell] - prices[buy]
                maxProfit = max(maxProfit, profit)
            #sell less than buy, able to lower buy, move buy to be sell
            else:
                buy = sell
            sell += 1
        return maxProfit
        