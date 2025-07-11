from typing import List
# Zachary West 07/11/2025
# First Solution Attempt Time: 4 mins

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        front = 0
        back = len(numbers) - 1

        #O(1) additional space requires the use of pointers instead of hash
        while (front < back):
            total = numbers[front] + numbers[back]
            if (total < target):
                front +=1
            elif (total > target):
                back -=1
            else:
                return [front+1,back+1]

