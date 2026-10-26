class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[right] < nums[mid]:
                left = mid + 1
            else:
                right = mid
        smallest = right

        if target > nums[-1]:
            first = 0
            last = smallest - 1
        elif target < nums[-1]:
            first = smallest
            last = len(nums) - 1
        else:
            return len(nums) - 1
        
        while first <= last:
            middle = (first + last) // 2
            if nums[middle] < target:
                first = middle + 1
            elif nums[middle] > target:
                last = middle - 1
            else:
                return middle
        return -1



        
        