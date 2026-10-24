class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        lst = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            start = i + 1
            end = len(nums) - 1        
            while start < end:
                if nums[start] + nums[end] < -(nums[i]):
                    start += 1
                elif nums[start] + nums[end] > -(nums[i]):
                    end -= 1
                else: 
                    lst.append([nums[start],nums[end],nums[i]])
                    start += 1
                    end -= 1
                    while start < end and nums[start] == nums[start - 1]:
                        start+= 1
                
        return lst