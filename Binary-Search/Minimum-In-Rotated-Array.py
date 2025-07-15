from typing import List
# Zachary West 07/15/2025
# First Solution Attempt Time: 19 mins
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        m = l + (r-l)//2

        while (l < r):
            med = nums[m]
            right = nums[r]
            if (med > right): # implies that the array restarts, min on right
                l = m + 1
            else: # otherwise min on left
                r = m 
            
            m = l + (r-l)//2
            
        return nums[l] 
                
    

                
        