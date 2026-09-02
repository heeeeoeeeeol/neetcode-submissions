class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [0]*(n)

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2: return False
        if self.size[p1] >= self.size[p2]: 
            self.parent[p2] = p1
            self.size[p1] += self.size[p2]
        else:
            self.parent[p1] = p2
            self.size[p2] += self.size[p1]
        return True

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        uf = DSU(ROWS*COLS+1)
        offset = [(1,0),(-1,0),(0,1),(0,-1)]

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    for dr,dc in offset:
                        if 0<=r+dr<ROWS and 0<=c+dc<COLS and board[r+dr][c+dc]=="O":
                            uf.union(r*COLS+c, (r+dr)*COLS+c+dc)
                    if r==0 or r==ROWS-1 or c==0 or c==COLS-1: uf.union(r*COLS+c, ROWS*COLS)

        p = uf.find(ROWS*COLS)
        for r in range(1, ROWS-1):
            for c in range(1, COLS-1):
                if board[r][c] == "O" and uf.find(r*COLS+c) != p: board[r][c] = "X"

