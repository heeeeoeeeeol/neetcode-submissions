class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [0]*n

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2: return False
        if self.size[p1] >= self.size[p2]: p1, p2 = p2, p1
        self.parent[p1] = p2
        self.size[p2] += self.size[p1]
        return True

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        uf = DSU(n*n)
        l = sorted([(grid[r][c],r,c) for c in range(n) for r in range(n)])

        offset = [(-1,0),(1,0),(0,1),(0,-1)]
        for t, r, c in l:
            for dr,dc in offset:
                if 0<=dr+r<n and 0<=dc+c<n and grid[r+dr][c+dc] <= t:
                    uf.union(n*r+c, n*(r+dr)+c+dc)           
            if uf.find(0) == uf.find(n*n-1): return t


        