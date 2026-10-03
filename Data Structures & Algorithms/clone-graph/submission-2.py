"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == None:
            return None
        
        hashMap = {}

        def clone(node):
            if node in hashMap:
                return

            hashMap[node] = Node()
            hashMap[node].val = node.val
            
            for n in node.neighbors:
                clone(n)
                hashMap[node].neighbors.append(hashMap[n])
            
        clone(node)
        return hashMap[node]
        
