from typing import Optional

# Zachary West 07/21/2025
# First Solution Attempt Time: 10 mins 
# Used hints to learn about the 2 ptr method for cycle detection


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow_ptr = head
        fast_ptr = head
    
        while fast_ptr and fast_ptr.next: #ensures access is safe
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

            if (fast_ptr == slow_ptr): return True
        return False # if it breaks, then it is not a cycle as fast_ptr found end
        