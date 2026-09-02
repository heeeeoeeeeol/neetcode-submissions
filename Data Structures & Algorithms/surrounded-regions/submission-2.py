class Solution:
    def solve(self, board: List[List[str]]) -> None:
        q = deque()
        ROWS, COLS = len(board), len(board[0])
        offset = [(1,0),(-1,0),(0,1),(0,-1)]

        for r in range(ROWS): 
            if board[r][0] == "O": q.append((r,0))
            if board[r][-1] == "O": q.append((r,COLS-1))
        for c in range(COLS): 
            if board[0][c] == "O": q.append((0,c))
            if board[-1][c] == "O": q.append((ROWS-1,c))

        while q:
            r,c = q.popleft()
            board[r][c] = "$"
            print(r,c,board[r][c])
            for dr,dc in offset:
                if 0<=r+dr<ROWS and 0<=c+dc<COLS and board[r+dr][c+dc]=="O":
                    q.append((r+dr,c+dc))

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c]=="O": board[r][c] = "X"
                elif board[r][c]=="$": board[r][c] = "O"

