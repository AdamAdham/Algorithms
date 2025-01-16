class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Intuition is that if the day before is smaller than current day we just buy previous day and sell current day
        # If previous is larger than current we dont buy or sell
        # this leads to optimal solution due to the unlimited buy/sell approach with no penalty on each action
        max = 0
        for i in range(1,len(prices)):
            diff = prices[i] - prices[i-1]
            if(diff>0):
                max += diff
        return max