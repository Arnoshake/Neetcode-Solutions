from typing import Optional

# Zachary West 07/21/2025
# First Solution Attempt Time: 8 mins 
# These easy neetcodes are proving difficult from a syntax standpoint


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node = ListNode() #dummy = head, node = curr

        while list1 and list2:
            if list1.val <= list2.val:
                node.next= list1
                list1 = list1.next
            else:
                node.next= list2
                list2 = list2.next
            node = node.next # must increment the sorted list to next object
        
        node.next = list1 or list2
        return dummy.next #returning dummy would provide a null value, start on first val after head