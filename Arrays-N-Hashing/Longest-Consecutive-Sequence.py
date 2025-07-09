from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_dict = {}
        for index,value in enumerate(nums): # O(N)
            my_dict[value] = index
        
        count = 0
        max_sequence = 0
        for val in my_dict: # O(N)
            if (val-1) not in my_dict:
                #start of sequence
                count = 1
                current = val
                while (current + 1) in my_dict:
                    #happens ONCE when its the start of a sequence...
                    # each number visited once TOTAL (making it equivalent to a seperate loop, O(N))
                    current +=1
                    count +=1
            
            max_sequence = max(max_sequence,count)
        return max_sequence # O(N + N + N) = O(N)



        