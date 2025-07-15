from typing import List
# Zachary West 07/15/2025
# First Solution Attempt Time: 13 mins
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        height = len(matrix) - 1
        width = len(matrix[0]) - 1
        rl = 0
        rh = height
        while (rl <= rh):
            rm = rl + (rh-rl)//2
            if ( matrix[rm][0] <= target <= matrix[rm][width]):
                # THE VALUE MAY EXIST IN THIS RANGE
                cl = 0
                ch = width
                while (cl <= ch):
                    cm = cl + (ch-cl)//2
                    if matrix[rm][cm] == target: return True
                    elif matrix[rm][cm] > target:
                        ch = cm - 1
                    else:
                        cl = cm + 1
                return False
            elif matrix[rm][0] > target:
                rh = rm - 1
            else:
                rl = rm + 1
        return False