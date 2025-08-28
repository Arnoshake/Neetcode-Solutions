from typing import List
# Zachary West 08/28/2025
# First Solution Attempt Time: 15 mins, using solution as learning for window concept
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        max_profit = 0
        while r < len(prices):
            bought,sold = prices[l],prices[r]
            if bought < sold: # a profit was made
                profit = sold - bought
                max_profit = max(max_profit,profit)
            else: #no profit was made, you need to try and buy on another day
                l = r
            r += 1 
        return max_profit


        