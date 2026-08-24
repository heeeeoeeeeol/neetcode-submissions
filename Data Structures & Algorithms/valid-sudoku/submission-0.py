class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        dicts = [{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}]
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    if dicts[0].get(board[i][j], 0) == 0: dicts[0][board[i][j]] = 1
                    else: 
                        return False      
                    if dicts[1+j].get(board[i][j], 0) == 0: dicts[1+j][board[i][j]] = 1
                    else: 
                        print(1+j)
                        return False      
                    if dicts[10+(i//3)*3+j//3].get(board[i][j], 0) == 0: dicts[10+(i//3)*3+j//3][board[i][j]] = 1
                    else: 
                        print(10+(i//3)*3+j//3)
                        return False      
            dicts[0] = {}
        return True