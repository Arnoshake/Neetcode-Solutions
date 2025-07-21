from typing import Optional

# Zachary West 07/21/2025
# First Solution Attempt Time: 15 mins --> Reviewed concepts of Linked Lists, never done in python


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        # A --> B --> C --> D
        #   prev (curr) next
        while curr: #will go until its None (past list by one)
            next_temp = curr.next # save rest of list
            curr.next = prev # break link & reverse the pointer
            prev = curr
            curr = next_temp #re assign current (restoring list)
        return prev # prev = new head when curr = None

            

        