class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        for i in range(len(nums)):
            dictionary[nums[i]] = i
        
        for i in range(len(nums)):
            find_number = target - nums[i]
            if find_number in dictionary and dictionary[find_number] != i:
                j = dictionary[target-nums[i]]
                return[i,j]


            
        