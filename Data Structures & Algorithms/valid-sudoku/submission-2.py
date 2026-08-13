class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''plan is to have a flagging array and then check for the
        conditions '''
        def checker(arr)->bool: #caution: takes integer array
            flag = [0] * 10  #starts from zero so index logic works
            for i in range(0,len(arr)):
                if flag[arr[i]] != 0:
                    return False
                else:
                    flag[arr[i]] = 1


        #checking columns and rows
        recordedColumn = []
        for i in range(0,9):
            for j in range(0,9):
                if board[j][i].isdigit():
                    recordedColumn.append(int(board[j][i]))
            if checker(recordedColumn) == False:
                return False
            recordedColumn = []

        recordedRow = []
        for i in range(0,9):
            for j in range(0,9):
                if board[i][j].isdigit():
                    recordedRow.append(int(board[i][j]))
            if checker(recordedRow) == False:
                return False
            recordedRow = []

        #checking 9 individual boxes with 9 for loops


        recordedBox = []
        for i in range(0,3):
            for j in range(0,3):
                if board[i][j].isdigit():
                    recordedBox.append(int(board[i][j]))
        if checker(recordedBox) == False:
            return False
        
        recordedBox = []
        for i in range(0,3):
            for j in range(3,6):
                if board[i][j].isdigit():
                    recordedBox.append(int(board[i][j]))
        if checker(recordedBox) == False:
            return False

        recordedBox = []
        for i in range(0,3):
            for j in range(6,9):
                if board[i][j].isdigit():
                    recordedBox.append(int(board[i][j]))
        if checker(recordedBox) == False:
            return False

        recordedBox = []
        for i in range(3,6):
            for j in range(0,3):
                if board[i][j].isdigit():
                    recordedBox.append(int(board[i][j]))
        if checker(recordedBox) == False:
            return False
        
        recordedBox = []
        for i in range(3,6):
            for j in range(3,6):
                if board[i][j].isdigit():
                    recordedBox.append(int(board[i][j]))
        if checker(recordedBox) == False:
            return False

        recordedBox = []
        for i in range(3,6):
            for j in range(6,9):
                if board[i][j].isdigit():
                    recordedBox.append(int(board[i][j]))
        if checker(recordedBox) == False:
            return False

        recordedBox = []
        for i in range(6,9):
            for j in range(0,3):
                if board[i][j].isdigit():
                    recordedBox.append(int(board[i][j]))
        if checker(recordedBox) == False:
            return False
        
        recordedBox = []
        for i in range(6,9):
            for j in range(3,6):
                if board[i][j].isdigit():
                    recordedBox.append(int(board[i][j]))
        if checker(recordedBox) == False:
            return False

        recordedBox = []
        for i in range(6,9):
            for j in range(6,9):
                if board[i][j].isdigit():
                    recordedBox.append(int(board[i][j]))
        if checker(recordedBox) == False:
            return False
        return True