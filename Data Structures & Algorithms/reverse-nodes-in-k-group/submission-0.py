# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


        ## check if aage k nodes hai bhi ki nahi
        ## reversal logic
        ## proper connection logic
        ## else condition if aage nodes lesser than k
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not(head):
            return head
        

        
        def check(node):
            curr = node
            count = 1
            while(curr.next) and (count < k):
                curr = curr.next
                count += 1
            
            if count == k:
                return curr
            else:
                return None
        
        def reversal(node, prev):
            curr = node
            count = 0
            while(curr) and (count < k):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
                count += 1
            return prev
    
        tail = check(head)
        if not tail:
            return head
        
        res = tail
        curr = head
        prev_tail = None

        while True:
            
            if not curr:
                break
            
            
            tail = check(curr)
            if not tail:
                break
            
            #node immediately after current groups tail
            next_group = tail.next
            new_head = reversal(curr, next_group)

            if prev_tail:
                prev_tail.next = new_head
            
            prev_tail = curr

            curr = next_group
        return res











            