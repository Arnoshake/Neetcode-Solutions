# Zachary West 07/08/2025
# First Solution Attempt Time: 23 mins
# Used ChatGPT for how to traverse for grids
from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #CHECK ROW FOR DUPLICATES
        for row in board: # O(N^2)
            curr_row = {i: 0 for i in range(1, 10)} # {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
            
            for number in row:
                
                if number == ".":continue
                num = int(number)
                if (curr_row[num] >=1): 
                    print("ROW FALSE")
                    return False
                else: curr_row[num] +=1
        #CHECK COL FOR DUPLICATES
        for col in range(9): # O(N^2)
            curr_col = {i: 0 for i in range(1, 10)} # {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
            for row in range(9):
                number = board[row][col]
                if number == ".":continue
                num = int(number)
                if (curr_col[num] >=1):
                    print("COL FALSE: ",curr_col)
                    return False
                else: curr_col[num] +=1
        #CHECK 3x3 GRIDS

        for row_start in [0, 3, 6]: # O( (sqrtN)^4 = O(N^2))
            for col_start in [0, 3, 6]:
                #top left of a 3x3 grid
                curr_grid = {i: 0 for i in range(1, 10)}
                for row in range(row_start,row_start+3):
                    for col in range(col_start,col_start+3):
                        number = board[row][col]
                        if number == ".":continue
                        num = int(number)
                        if curr_grid[num] >= 1:
                            print("GRID FALSE")
                            return False
                        else: curr_grid[num] +=1
                        #iterates through 3x3 grid
        
        return True # O(3N^2)

        

        