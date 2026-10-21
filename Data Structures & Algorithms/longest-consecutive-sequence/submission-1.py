class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)

        length = 0
        maximum = 0
        for num in nums:
            if num - 1 not in nums_set:

                length = 1
                number = num

                while number + 1 in nums_set:
                    length += 1
                    number +=1

                maximum = max(length,maximum)

        return maximum
