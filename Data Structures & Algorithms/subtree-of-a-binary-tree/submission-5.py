# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        ## basically find the node with the same value
        ## when found start checking if the tree is the same or not
        ## will not contain repeated values as its binary tree
        node = []
        def find(root):
            nonlocal node
            if (root.val == subRoot.val):
                node.append(root)
            if root.left:
                find(root.left)
            if root.right:
                find(root.right)
        
        find(root)
        
        if (len(node) != 0):
            def check(node1, node2):
                if (not node1) and (not node2):
                    return True
                if (not node1) or (not node2) or (node1.val != node2.val):
                    return False
                
                return check(node1.left, node2.left) and check(node1.right, node2.right)
            
            for n in node:
                if check(n, subRoot):
                    return True
            else: return False
        else: return False

            
    
            
            

            