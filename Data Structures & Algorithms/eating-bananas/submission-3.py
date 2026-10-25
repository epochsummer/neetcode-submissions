class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maximum = max(piles)
        minimum = 1

        while minimum < maximum:
            total = 0
            middle = (maximum + minimum) // 2
            for i in piles:
                total += (i + middle - 1) // middle
            if total <= h:
                maximum = middle
            else:
                minimum = middle + 1
        return minimum
        