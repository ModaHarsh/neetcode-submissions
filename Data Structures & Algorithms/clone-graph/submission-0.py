"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        hashmap = {}
        curr = node

        if node == None:
            return None

        def clone(node):
            if node not in hashmap:
                hashmap[node] = Node()
                hashmap[node].val = node.val
            
            for n in node.neighbors:
                if n in hashmap:
                    hashmap[node].neighbors.append(hashmap[n])
                    continue
                hashmap[node].neighbors.append(clone(n))
            
            return hashmap[node]
        
        return clone(node)
        