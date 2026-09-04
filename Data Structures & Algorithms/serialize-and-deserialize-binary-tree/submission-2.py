# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        master = ""
        def dfs(root):
            nonlocal master
            if not root:
                master += "N,"
                return None
            
            master += (str(root.val) + ",")
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return master
    # serialize basically gives preorder traversal


    def deserialize(self, data: str) -> Optional[TreeNode]:
        index = 0
        order = data.split(",")
        def dfs(order):
            nonlocal index
            
            if index >= len(order):
                return None
            if order[index] == "N":
                index += 1
                return None
            
            
            root = TreeNode(order[index])
            index += 1
            
            root.left = dfs(order[index:])
            root.right = dfs(order[index:])
            
            return root

        dfs(order)
        return root
            
            




            




