class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1]*n

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
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        uf = DSU(len(grid)*len(grid[0]))
        temp = []
        for row in grid: temp += row
        uf.size = temp
        offset = [(1,0),(-1,0),(0,1),(0,-1)]

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    for x, y in offset:
                        if 0<=r+y<len(grid) and 0<=c+x<len(grid[0]) and grid[r+y][c+x] == 1:
                            uf.union(r*len(grid[0])+c, (r+y)*len(grid[0])+c+x)
        return max(uf.size)
                            


