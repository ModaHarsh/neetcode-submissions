# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val
        def maxGain(root):
            nonlocal res
            if not root:
                return 0
            
            left = max(maxGain(root.left), 0)
            right = max(maxGain(root.right), 0)

            res = max(res, root.val + left + right)
            
            return root.val + max(left,right)
        maxGain(root)
        return res