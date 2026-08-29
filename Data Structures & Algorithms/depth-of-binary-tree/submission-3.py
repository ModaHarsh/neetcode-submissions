# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        count = 0
        if (root):
            count = 1
        else:
            return 0
        maxHeight = 0

        def dfs(node):
            nonlocal count
            nonlocal maxHeight
            curr = node

            if (not(curr.left) and not(curr.right)):
                if count > maxHeight:
                    maxHeight = count
                count -= 1
                return None
                        
            if (curr.left):
                count += 1
                dfs(curr.left)

            if (curr.right):
                count += 1
                dfs(curr.right)

            count -= 1
            
        dfs(root)
        return maxHeight


