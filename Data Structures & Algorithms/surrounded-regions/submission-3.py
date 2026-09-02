class Solution:
    def solve(self, board: List[List[str]]) -> None:
        vis, ROWS, COLS = set(), len(board), len(board[0])
        def dfs(r,c):
            if not(0<=r<ROWS and 0<=c<COLS) or board[r][c]=="X" or (r,c) in vis: return
            vis.add((r,c))
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)

        for r in range(ROWS): 
            if board[r][0] == "O": dfs(r,0)
            if board[r][-1] == "O": dfs(r,COLS-1)
        for c in range(COLS): 
            if board[0][c] == "O": dfs(0,c)
            if board[-1][c] == "O": dfs(ROWS-1,c)

        for r in range(1, ROWS-1):
            for c in range(1, COLS-1):
                if board[r][c]=="O" and (r,c) not in vis:
                    board[r][c] = "X"
