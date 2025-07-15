from typing import List
# Zachary West 07/15/2025
# First Solution Attempt Time: 7 mins
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while ( l <= r):
            guess_index = l + (r-l)//2
            guess =nums[guess_index]
            if guess == target: return guess_index
            elif guess > target:
                r = guess_index - 1
            else:
                l = guess_index + 1
        return -1

        