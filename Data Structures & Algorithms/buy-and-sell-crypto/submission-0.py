class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        TC: O(n)
        SC: O(1)
        """

        minimum = max(prices)
        N = len(prices)
        profit = 0

        for i in range(N):
            minimum = min(minimum, prices[i])
            profit = max(profit, prices[i]-minimum)

        return profit
        