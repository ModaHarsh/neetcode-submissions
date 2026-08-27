"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not(head):
            return None
        
        curr = head
        prev = None
        head2 = None
        hashMap = {}
        while(curr):
            newNode = Node(curr.val)
            if not(head2):
                head2 = newNode
                prev = head2
                hashMap.setdefault(curr, newNode)
                curr = curr.next
                continue
            prev.next = newNode
            prev = newNode
            hashMap.setdefault(curr, newNode)
            curr = curr.next
        prev.next = None

        curr = head
        curr2 = head2
        while(curr):
            i = curr
            i = i.random
            if not (i):
                curr2.random = None
                curr = curr.next
                curr2 = curr2.next
                continue
            curr2.random = hashMap[i]
            curr = curr.next
            curr2 = curr2.next
        return head2


