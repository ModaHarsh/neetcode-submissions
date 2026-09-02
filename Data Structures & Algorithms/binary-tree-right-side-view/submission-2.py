# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        ## trying bfs approach
        ## last node of every level is going to be our right side view for that level
        ## level order traversal
        if not root:
            return []
        res = []
        q = deque([root])

        while (q):
            rightRoot = None
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    rightRoot = node
                    q.append(node.left)
                    q.append(node.right)
            if rightRoot:
                res.append(rightRoot.val)
        return res
                
        