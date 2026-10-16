class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        count_zero = 0
        for i in nums:
            if i == 0:
                count_zero += 1

        if count_zero > 1:
            return [0]*len(nums)

        if count_zero == 0:
            multiply = nums[0] 
            lst = []
            for i in range(1,len(nums)):
                multiply *= nums[i]
            for i in nums:
                total = int(multiply / i)
                lst.append(total)
        else:
            zero_index = 0

            for i in range(len(nums)):
                if nums[i] == 0:
                    zero_index = i
            
            if nums[0] != 0:
                multiply = nums[0]
                for i in range(1,len(nums)):
                    if nums[i] != 0:
                        multiply *= nums[i]
            
            else:
                multiply = nums[1]
                if len(nums) > 2:
                    for i in range(2,len(nums)):
                        if nums[i] != 0:
                            multiply *= nums[i]

            lst = [0] * len(nums)
            lst[zero_index] = multiply
            return lst

        return lst