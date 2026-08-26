# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #okay h1 and h2 given to us
        c1 = list1
        c2 = list2
        head = None

        if (c1) and not (c2):
            return c1
        elif not (c1) and (c2):
            return c2

        while ((c1) and (c2)):         #if one of the list DNE situtation
            if not (head):
                if(c1.val < c2.val):
                    head = c1
                    c1 = c1.next
                    curr = head
                    continue
                else:
                    head = ListNode(c2.val)
                    c2 = c2.next
                    curr = head
                    continue
            
            if(c1.val < c2.val):
                curr.next = c1
                c1 = c1.next
                curr = curr.next
            elif(c1.val >= c2.val):
                curr.next = c2
                c2 = c2.next
                curr = curr.next
        
        if (c1):        #c1 still exists
            curr.next = c1
        elif (c2):
            curr.next = c2
        return head

            



            
            



