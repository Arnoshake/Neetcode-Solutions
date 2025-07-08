from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_map = {}
        # key: number, value: frequency

        #Frequency gives priority to bucket sort over counting sort
        #populate dictionary
        for value in nums:                                  # O(N) time and space
            if value in frequency_map:
                frequency_map[value] += 1
            else:
                frequency_map[value] = 1
        
        #create/populate bucket representation
        
        buckets = [ [] for _ in range (len(nums) + 1)]
        for key,value in frequency_map.items():              # O(N) time and space
            buckets[value].append(key)
        #traverse bucket and return the k most frequent
        
        solution = []
        for i in range(len(buckets) - 1, -1, -1):           #  best: O(K) worst: O(N) // O(N) Space. (k <= n)
            for numbers in buckets[i]:                      
                if (len(solution) == k): return solution
                solution.append(numbers)
                if (len(solution) == k): return solution

#SOLUTION BIG O : BESTCASE = O(N + K), WORSECASE = O(N + N) --> All cases simplify to O(N)
#SOLUTION SPACE COMPLEXITY : O(N)

            

