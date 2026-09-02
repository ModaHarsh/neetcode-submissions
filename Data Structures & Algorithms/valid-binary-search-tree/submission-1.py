# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ## but complexity given to us as O(n)
        ## we can do preordertraversal store values
        ## and then check if the tree is sorted or not
        arr = []
        def preorder(root):
            nonlocal arr
            if not root:
                return None
            preorder(root.left)
            arr.append(root.val)
            preorder(root.right)
        preorder(root)
        

        def isSorted(arr):
            for i in range(len(arr) - 1):
                if arr[i] >= arr[i + 1]:
                    return False
            else: return True 

        return isSorted(arr)      

        