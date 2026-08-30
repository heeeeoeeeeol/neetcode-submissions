class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(r, c):
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0])) or grid[r][c] != 1: 
                return 0
            grid[r][c] = 0
            return 1 + dfs(r-1,c) + dfs(r+1,c) + dfs(r,c-1) + dfs(r,c+1)
            
        m = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                m = max(m, dfs(r,c))

        return m