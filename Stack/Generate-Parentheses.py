from typing import List
# Zachary West 07/10/2025
#First Solution Attempt Time: 18 mins (help from solution video)
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        solution = []

        def backtrack(openN,closeN):
            if openN == closeN == n: #all () pairs used... root of recursion
                solution.append("".join(stack)) #combine array of parantheses into string with no gap
                return
            if openN < n:
                stack.append("(")
                backtrack(openN+1,closeN)
                stack.pop()
            if closeN < openN:
                stack.append(")")
                backtrack(openN,closeN+1)
                stack.pop()
        backtrack(0,0)
        return solution


        