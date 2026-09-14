class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        TC: O(n)
        SC: O(1)
        """
        
        buy = prices[0]
        profit = 0
        N = len(prices)

        for i in range(N):
            buy = min(prices[i], buy) ## Should be lowest
            profit = max((prices[i]-buy), profit)

        return profit
