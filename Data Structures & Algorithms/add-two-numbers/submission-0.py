# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        ## this can be done with the help of string operations on the listNode.val
        s1 = ""
        s2 = ""
        c1 = l1
        c2 = l2
        while(c1):
            s1 += (str(c1.val))
            c1 = c1.next
        while(c2):
            s2 += (str(c2.val))
            c2 = c2.next

        s1 = s1[::-1]
        s2 = s2[::-1]
        
        sum = int(int(s1) + int(s2))
        sum = str(sum)
        sum = sum[::-1]
        revList = list(sum)
        
        head = None
        
        for i in revList:
            if not(head):
                head = ListNode()
                head.val = i
                head.next = None
                curr = head
                continue
            
            curr.next = ListNode()
            curr = curr.next
            curr.val = i
        
        return head




