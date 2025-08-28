class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        l = 0
        solution = 0

        for r in range(len(s)):
            current_character = s[r]
            while current_character in char_set:
                # a duplicate exists within this window, shift left until past it
                char_set.remove(s[l])
                l += 1
            #duplicates of the current character are removed, safe to add
            char_set.add(current_character)
            solution = max(solution, (r-l)+1)
        return solution
        