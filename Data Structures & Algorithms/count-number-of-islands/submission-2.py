class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1]*n

    def find(self, node):
        if self.parent[node] != node:
            return self.find(self.parent[node])
        return node

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
    def numIslands(self, grid: List[List[str]]) -> int:
        d = DSU(len(grid)*len(grid[0]))
        ic = 0  

        offset = [(-1,0),(1,0),(0,-1),(0,1)]

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    ic += 1
                    for x,y in offset:
                        if 0 <= r+y < len(grid) and 0 <= c+x < len(grid[0]) and grid[r+y][c+x] == "1": 
                            if d.union(r*len(grid[0])+c, (r+y)*len(grid[0])+c+x): ic -= 1

        
        return ic                  






        