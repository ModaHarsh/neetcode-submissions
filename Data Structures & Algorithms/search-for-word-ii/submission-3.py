class PrefixTrie:
    def __init__(self):
        self.children = {}
        self.isEnding = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = PrefixTrie()
        
        for word in words:
            curr = root
            for c in word:
                if c not in curr.children:
                    curr.children[c] = PrefixTrie()
                curr = curr.children[c]
            curr.isEnding = True
        
        R = len(board)
        C = len(board[0])
        res = []
        def dfs(row, col, string, curr):
            
            if board[row][col] not in curr.children:
                return

            if board[row][col] in curr.children:
                
                curr = curr.children[board[row][col]]
                string += board[row][col]
                
                if curr.isEnding:
                    res.append(string)
                    curr.isEnding = False
                
                temp = board[row][col]
                board[row][col] = "#"
                if row != 0:    ## going up
                    dfs(row - 1, col, string, curr)   
                if row != R - 1:    ## going down
                    dfs(row + 1, col, string, curr)
                if col != 0:    ## going left
                    dfs(row, col - 1, string, curr)
                if col != C - 1:    ## going right
                    dfs(row, col + 1, string, curr)
                board[row][col] = temp
            
            

        for r in range(0,R):
            for c in range(0,C):
                dfs(r,c,"",root)
        return res