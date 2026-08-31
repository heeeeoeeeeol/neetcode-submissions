class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        vis = set()
        q = deque()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if not grid[r][c]: 
                    q.append((r,c,0))

        while q:
            r,c,d = q.popleft()
            if not (0<=r<len(grid) and 0<=c<len(grid[0])) or (r,c) in vis or grid[r][c] == -1: continue
            vis.add((r,c))
            grid[r][c] = d
            q.append((r+1,c,d+1))
            q.append((r-1,c,d+1))
            q.append((r,c+1,d+1))
            q.append((r,c-1,d+1))
            