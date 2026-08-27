# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        curr = head
        lenList = 0           # total nodes in list
        while(curr):
            curr = curr.next
            lenList += 1

        # 1_index of node to be removed
        count = lenList - n
        # counts equals ths 1_starting index of the node just 
        # before the node to be removed

        index = 1
        curr = head
        if count == 0:
            head = curr.next
            return head
        if count == 0 and lenList == 1:
            head = None
            return head

        while(index != count):
            curr = curr.next
            index += 1
        
        curr.next = curr.next.next
        return head