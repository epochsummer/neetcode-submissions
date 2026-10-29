class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = prices[0]
        maximum = 0

        for price in prices:
            minimum = min(price,minimum)

            profit = price - minimum    
            maximum = max(profit,maximum)

        
        return maximum


