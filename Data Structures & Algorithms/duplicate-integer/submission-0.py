class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dictionary = {}
        for i in nums:
            if i in dictionary:
                return True
            else:
                dictionary[i] = 1
        return False
        