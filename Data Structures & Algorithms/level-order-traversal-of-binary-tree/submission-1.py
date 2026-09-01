# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ## simple Bredth first search will do here
        q = deque()
        res = []
        sub = []
        if root:
            q.append(root)
        
        while(q):
            for node in q:
                sub.append(node.val)
            res.append(sub)
            sub = []
            for _ in range(len(q)):
                curr = q.popleft()
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

        return res
        # state of q before every for loop
        # iteration is our level sequence



        