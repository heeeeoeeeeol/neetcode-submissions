class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        fresh = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
               if grid[r][c] == 1: fresh += 1
               elif grid[r][c] == 2: q.append((r,c))

        offset = [(-1,0),(1,0),(0,1),(0,-1)]

        lvl = 0
        while q and fresh:
            for _ in range(len(q)):
                r, c = q.popleft()
                for x,y in offset:
                    if 0<=r+y<len(grid) and 0<=c+x<len(grid[0]) and grid[r+y][c+x] == 1:
                        q.append((r+y,c+x))
                        grid[r+y][c+x] = 2
                        fresh -= 1
            lvl += 1

        return lvl if fresh == 0 else -1