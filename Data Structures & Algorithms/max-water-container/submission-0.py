class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximum = -1
        left = 0
        right = len(heights) - 1
        while left < right:
            area = (right - left) * min(heights[left] , heights[right])
            maximum = max(area,maximum)
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        return maximum            
