from typing import List
# Zachary West 07/14/2025
# First Solution Attempt Time: 30 mins
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        solutions = []
        for i in range(len(nums)):
            if (i > 0 and nums[i] == nums[i-1]):
                continue #skips duplicate
            left = i + 1
            right = len(nums) - 1

            while (left < right):
                total = nums[i] + nums[left] + nums[right]
                if (total == 0):
                    solutions.append((nums[i],nums[left],nums[right]))
                    while (left < right and nums[left] == nums[left +1]): left +=1
                    while (right > left and nums[right] == nums[right - 1]): right -=1
                    #regardless, must increment
                    right -=1
                    left +=1
                elif total < 0: left +=1
                else: right -=1
        return solutions


        