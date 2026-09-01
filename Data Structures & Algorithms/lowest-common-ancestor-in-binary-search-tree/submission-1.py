# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        ## for lowest common ancestor
        ## one node should be in the left subtree
        ## another node should be in the right subtree
        ## can figure out which subtree to find node in using BST conditions        
        curr = root
        while True:
            if curr.val > max(p.val, q.val):
                curr = curr.left
            elif curr.val < min(p.val, q.val):
                curr = curr.right
            else:
                return curr
