# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ## can just do preorder traversal and return the kth array element
        ## trying with a different apporach but that uses similar preorder logic
        ## although
        leaf = None
        count = 0
        val = -1
        def calls(root):
            nonlocal leaf
            nonlocal count
            nonlocal val

            if not root:
                return None
            
            
            
            calls(root.left)
            count += 1
            if count == k:
                val = root.val
            calls(root.right)

            

        calls(root)
        return val

