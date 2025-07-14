from typing import List
# Zachary West 07/14/2025
# First Solution Attempt Time: 15 mins
# O(N), O(1) space
class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left = 0
        right = len(heights) - 1
        max_volume = 0
        while (left < right): # O(N)
            max_height = min(heights[left],heights[right])
            width = right - left
            volume = width * max_height
            if volume > max_volume:
                max_volume = volume
            
            if (heights[left] == max_height): left +=1
            else: right -=1
        return max_volume
        