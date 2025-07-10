# Zachary West 07/09/2025
# First Solution Attempt Time: 15 mins
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_pairs = {}
        bracket_pairs["}"] = "{"
        bracket_pairs["]"] = "["
        bracket_pairs[")"] = "("
        for c in s: # O(N)
            if (c in bracket_pairs.values()): #open bracket 
                stack.append(c)
            if c in bracket_pairs: #close bracket 
                if not stack or stack.pop() != bracket_pairs[c]:
                    return False
        return not stack # O(N)

    
        