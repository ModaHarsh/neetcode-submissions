# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        flag = 1
        def dfs(root):
            nonlocal flag
            if not root:
                return 0
            
            right = dfs(root.right)
            left = dfs(root.left)
            
            if abs(left - right) > 1:
                flag = 0
            
            return 1 + max(left, right)
        
        dfs(root)
        if flag == 1:
            return True
        else:
            return False
        