class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy = max(prices)
        profit = 0
        N = len(prices)

        for i in range(N):

            buy = min(prices[i], buy) ## Should be lowest
            profit = max((prices[i]-buy), profit)

        return profit
