# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ## find height of lSubtree then rSubtree
        ## sum it up save as max
        ## go move towards larger subtree and repeat till you reach
        ## a leaf node
        if not root:
            return None
        
        def dfs(node):
            if not node:
                return 0
            return 1 + max(dfs(node.left), dfs(node.right))
        
        maxDia = dfs(root) - 1
        curr = root
        currMax = maxDia
        while True:
            hLeft = dfs(curr.left)
            hRight = dfs(curr.right)
            currMax = hLeft + hRight
            
            if currMax > maxDia:
                maxDia = currMax
            
            if hLeft > hRight:
                curr = curr.left
            elif hLeft < hRight:
                curr = curr.right
            else:
                break
        return maxDia






            
                
        