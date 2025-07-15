from typing import List
# Zachary West 07/15/2025
# First Solution Attempt Time: 25 mins
# Used ChatGPT for conceptual explanation
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        # KEY IDEA IN ROTATED ARRAYS IS THAT A PORTION IS GUARANTEED SORTED <-- GPT
        while (l <= r):
            m = l + (r - l)//2

            if nums[m] == target: return m

            if nums[m] > nums[r]: # LEFT IS SORTED
                if (nums[l] <= target <= nums[m]):
                    r = m - 1
                else:
                    l = m + 1
            else:   #LEFT SIDE HAS START
                if (nums[m] <= target <= nums[r]):
                    l = m + 1
                else:
                    r = m - 1
        return -1
        