# Zachary West 07/08/2025
# First Solution Attempt Time: 43 mins
from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix_array = [0] * len(nums)
        suffix_array = [0] * len(nums)

        # POPULATING PREFIX 
        for index in range(len(nums)): # O(N)
            if index == 0:
                prefix_array[0] = 1 #1 bc dealing with products
                #no prefix at first index
                continue
            if index == 1:
                prefix_array[1] = nums[0]
                continue
            prefix_array[index] = prefix_array[index - 1] * nums[index - 1]
        # POPULATING SUFFIX 
        for index in range(len(nums) - 1, -1, -1): # O(N)
            if index == (len(nums) - 1):
                suffix_array[index] = 1
                #no suffix at last index
                continue
            if index == (len(nums) - 1) - 1:
                suffix_array[index] = nums[index + 1]
                continue
            suffix_array[index] = suffix_array[index + 1] * nums[index + 1]
        
        solution = [0] * len(nums)
        for index in range(len(nums)): # O(N)
            solution[index] = prefix_array[index] * suffix_array[index]
        return solution # TIME & SPACE = O(N + N + N) 
        
       