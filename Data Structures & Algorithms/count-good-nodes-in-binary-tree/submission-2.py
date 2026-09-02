# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        ## okay so for dfs everyNode
        ## should have a value larger than or equal to
        ## the current max seen so far
        res = 0
        maxSoFar = -101
        def dfs(root, maxSoFar):
            if not root:
                return 0
            
            if root.val >= maxSoFar :
                res = 1
            else:
                res = 0
            
            maxSoFar = max(root.val, maxSoFar)
            
            
            res += dfs(root.left, maxSoFar) + dfs(root.right, maxSoFar)
            
            
            return res
        
        
        return dfs(root, root.val)

        
            
        