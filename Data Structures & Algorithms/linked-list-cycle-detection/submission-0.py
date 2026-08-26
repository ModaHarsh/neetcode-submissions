# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        ## we have been given max count of the list as 1000
        ## so a simple counter would work

        curr = head
        count = 0
        while (curr) and (count <= 1000):
            count += 1       
            curr = curr.next
        
        if not(curr):
            return False
        else:
            return True
        

         