# Zachary West 07/11/2025
# First Solution Attempt Time: 21 mins (Distracted by Modern Family)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        front = 0
        back = len(s) - 1 
        while front <= back: #O(N)
            if (s[front].isalnum()):
                if (s[back].isalnum()):
                    #Both are actual letters
                    if (s[front].lower() != s[back].lower()):
                        print(s[front]," ",s[back])
                        return False
                    back -=1
                    front +=1
                else:
                    back -=1
            else:
                front +=1
            
        return True
        