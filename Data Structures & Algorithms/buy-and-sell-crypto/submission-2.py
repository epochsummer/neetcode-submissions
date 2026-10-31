class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum = 0
        minimum = prices[0]
        for i in range(1,len(prices)):
            minimum = min(minimum,prices[i])
            maximum = max(maximum,prices[i] - minimum)
        return maximum



        