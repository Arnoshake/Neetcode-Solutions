class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        
        # BRUTE FORCE SOLUTION --> Fails case 2 (runtime error)
        # Create an array of the size of nums+1 to represent the possible number range
        countArr = [0] * ( len(nums) + 1 ) # O(1)
        # iterate through nums and increment the new array at index = to value of nums
        for value in nums: # O(N)
            countArr[value] += 1
        # iterate through new array k times, finding the maximum and then setting that increment value to 0
        solution = []
        for i in range(k): #O(K)
            max_val = max(countArr) #O(N)
            max_val_index = countArr.index(max_val) #O(N)
            countArr[max_val_index] = -1 # set low for next iteration to find next max
            solution.append(max_val)
        # return an array of the solution
        return solution # O(N) + O(K * N) 
        








        