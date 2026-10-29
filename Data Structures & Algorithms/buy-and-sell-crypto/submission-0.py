class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = prices[0]
        maximum = 0

        for price in prices:
            profit = price - minimum    
            maximum = max(profit,maximum)

            minimum = min(price,minimum)
        
        return maximum


