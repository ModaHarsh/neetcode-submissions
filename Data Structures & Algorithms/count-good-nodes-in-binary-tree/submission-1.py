# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        ## good node if tree contains no
        ## node greater than the value of node in the path
        
        ## looks like a stack application problem
        ## so basically every new node in dfs should be greater than the
        ## previous node --

        stack = []
        count = 0
        def dfs(root):
            nonlocal count
            nonlocal stack
            if not root:
                return None

            if len(stack) == 0:
                count += 1
                stack.append(root)  
            
            elif root.val >= stack[-1].val:
                stack.append(root)
                count += 1
            
            dfs(root.left)
            dfs(root.right)
            if root == stack[-1]:
                stack.pop()
        
        dfs(root)
        return count










            
            