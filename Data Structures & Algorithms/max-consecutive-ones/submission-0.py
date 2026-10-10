class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maximum_count = 0
        for i in nums:
            if i != 1:
                if count > maximum_count:
                    maximum_count = count
                count = 0
            else:
                count += 1
        if count > maximum_count:
            maximum_count = count
        return maximum_count
        