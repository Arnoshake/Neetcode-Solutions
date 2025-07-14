from typing import List
# Zachary West 07/14/2025
# First Solution Attempt Time: 33 mins
# O(3N), O(3N) space
class Solution:
    def trap(self, height: List[int]) -> int:
        prefix_arr = [0] * len(height)
        prefix_arr[0] = 0
        suffix_arr = [0] * len(height)
        suffix_arr[(len(height) - 1)] = 0 
        for i in range(len(height)): #O(N)
            #at each column, find the heights of surrounding columns (prefix, suffix approach)
            if (i == 0): continue
            elif (i == 1):
                prefix_arr[1] = height[0]
            else:
                prefix_arr[i] = max(prefix_arr[i-1],height[i-1])


        for i in range(len(height) - 1, -1, -1): #O(N)
            if i == len(height) - 1:
                suffix_arr[i] = 0
            elif i == len(height) - 2:
                suffix_arr[i] = height[(len(height) - 1)]
            else:
                suffix_arr[i] = max(suffix_arr[i+1],height[i+1])
        
        solution = 0
        print(prefix_arr)
        print(suffix_arr)
        test = []
        for i,h in enumerate(height): #O(N)
            rain = min(prefix_arr[i], suffix_arr[i]) - h
            if (rain > 0):
                solution += rain
            test.append(rain)
        print(test)
        return solution #O(3N)