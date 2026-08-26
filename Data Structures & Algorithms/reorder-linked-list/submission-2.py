# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
    ## 0 1 2 3 4 5 6
    ## 0 6 1 5 2 4 3

    ## 0 1 2 3 4 5
    ## 0 5 1 4 2 3 

    ## okay so a mentioned in the hint you are basically reversing
    ## the second half of the list and then merging the lists
        if (head.next == None):
            return None

        curr = head
        count = 0
        while(curr):
            count += 1
            curr = curr.next
    
        half = (count + 1) // 2
    
        curr = head
        for i in range(half - 1):
            curr = curr.next
        nxt = curr.next
        curr.next = None

        #reversing the second list
        h2 = nxt
    
        curr = h2
        prev = None
        while(curr.next):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
    
        curr.next = prev
    
        h2 = curr

        c1 = head
        c2 = h2
        while (c1) and (c2):
            c1nxt = c1.next
            c2nxt = c2.next
            c1.next = c2
            c2.next = c1nxt
            pc1 = c1
            pc2 = c2
            c1 = c1nxt
            c2 = c2nxt
        
    



    



        