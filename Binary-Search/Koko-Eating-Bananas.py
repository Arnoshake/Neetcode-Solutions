from typing import List
import math
# Zachary West 07/15/2025
# First Solution Attempt Time: 23 mins
    # Used ChatGPT for conceptual understanding, code written by me
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # IF A SPEED IS TOO SLOW, ALL SPEEDS BEFORE IT ARE TOO SLOW
            # ^^^ BINARY SEARCH
        # THE FASTEST SPEED IS = LARGEST PILE ==> 1HR/PILE

        l = 1 #slowest speed is 1 banana
        r = max(piles)
        max_speed = r #fastest possible

        while (l <= r):
            k = l + (r-l)//2 # speed attempt/try
            tot_hours = 0
            for pile in piles:
                tot_hours += math.ceil(pile/k) # time per pile = bananas / time, ronuded up per instruction
            if tot_hours > h: #TOO SLOW
                l = k + 1 #increase the bottom boundary on possible speeds
            else: #fast enough...
                if max_speed > k:
                    max_speed = k
                r = k - 1
        return max_speed




            
        