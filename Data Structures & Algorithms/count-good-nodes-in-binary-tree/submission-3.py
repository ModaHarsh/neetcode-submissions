# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return None
        count = 0
        q = deque()
        q.append((root, float("-inf")))

        while (q):
            node, maxVal = q.popleft()
            if node.val >= maxVal:
                count += 1
                maxVal = node.val
            
            if node.left:
                q.append((node.left, maxVal))
            if node.right:
                q.append((node.right, maxVal))
        
        return count

