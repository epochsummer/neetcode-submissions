class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maximum_count = 0
        for i in nums:
            if i != 1:
                count = 0
            else:
                count += 1
            maximum_count = max(count,maximum_count)
        return maximum_count
        