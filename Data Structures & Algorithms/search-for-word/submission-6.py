class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def check(row, col, i):
            if i == len(word):
                return True

            temp = board[row][col]
            board[row][col] = "#"
            if col < len(board[0]) - 1:
                if board[row][col + 1] == word[i]:
                    if check(row, col + 1, i + 1):
                        return True
            if col > 0:
                if board[row][col - 1] == word[i]:
                    if check(row, col - 1, i + 1):
                        return True
            if row < len(board) - 1:
                if board[row + 1][col] == word[i]:
                    if check(row + 1, col, i + 1):
                        return True
            if row > 0:
                if board[row - 1][col] == word[i]:
                    if check(row - 1, col, i + 1):
                        return True
            board[row][col] = temp
            return False

        for y in range(len(board)):             # y - row
            for z in range(len(board[0])):         # z - col
                if board[y][z] == word[0]:
                    if check(y, z, 1):
                        return True
        else: return False


## overall idea is to iterate through the board
## whenever the first match is found
## then call check to see if that element can form a solution
## if yes then we can return true

## or then run further iterations to find the first match on the board